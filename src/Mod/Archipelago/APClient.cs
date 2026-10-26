using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;


namespace APKingdom2Crown.Archipelago
{
    public class APConnection
    {
        private static readonly ConcurrentQueue<long> PendingItems = new();
        private static readonly ConcurrentQueue<DeathLink> PendingDeathLinks = new();

        public ArchipelagoSession Session { get; private set; }
        private DeathLinkService DeathLinkService { get; set; }
        public bool Connected => Session?.Socket?.Connected ?? false;

        public async Task<bool> Connect(string address, string slotName, string password = "")
        {
            try
            {
                if (!Connected)
                {
                    Plugin.Log.LogInfo($"[AP] Opening a session for {slotName} at {address}.");

                    Session = ArchipelagoSessionFactory.CreateSession($"{address}");
                    Session.Socket.SocketClosed += SocketClosed;
                    Session.Socket.ErrorReceived += ErrorReceived;
                    Session.Items.ItemReceived += OnItemReceived;
                    Session.Socket.PacketReceived += OnPacktRevieved;

                    Plugin.Log.LogInfo($"Caugh a Session = {Session != null}");
                }
                //the Connect trigger OperationCanceledException causing a "Time out"
                LoginResult result = await Task.Run(() => Session.TryConnectAndLogin(
                    "Kingdom Two Crowns",     // game name (must match your server-side name)
                    slotName,
                    ItemsHandlingFlags.AllItems,
                    new Version("0.6.8"),
                    new string[] { "NoText" },
                    null,
                    password,
                    true
                ));

                if (result is LoginSuccessful success)
                {
                    Plugin.ApplySlotData(success.SlotData);
                    ConfigureDeathLink(Plugin.DeathLinkMode);
                    Plugin.Log.LogInfo($"[AP] Connected as {success.Slot} in team {success.Team}");
                    return true;
                }
                else
                {
                    var failure = (LoginFailure)result;
                    Session = null;
                    Plugin.Log.LogError($"[AP] Login failed: {string.Join(", ", failure.Errors)}");
                    return false;
                }
            }
            catch (Exception ex)
            {
                Plugin.Log.LogError($"[AP] Connection failed: {ex}");
                return false;
            }
        }

        private void ConfigureDeathLink(int mode)
        {
            if (Session == null) return;
            try
            {
                DeathLinkService = Session.CreateDeathLinkService();
                DeathLinkService.OnDeathLinkReceived += deathLink => PendingDeathLinks.Enqueue(deathLink);
                if (mode > 0)
                {
                    DeathLinkService.EnableDeathLink();
                    Plugin.Log.LogInfo($"[AP] DeathLink enabled from YAML (mode {mode}).");
                }
                else
                {
                    DeathLinkService.DisableDeathLink();
                    Plugin.Log.LogInfo("[AP] DeathLink is disabled by the generated YAML.");
                }
            }
            catch (Exception ex)
            {
                Plugin.Log.LogError($"[AP] Could not configure DeathLink: {ex}");
            }
        }

        public void SendDeathLink(string cause)
        {
            if (DeathLinkService == null || !Connected || Plugin.DeathLinkMode <= 0) return;
            try
            {
                string source = Plugin.ConfigSlot?.Value ?? "Kingdom Two Crowns";
                DeathLinkService.SendDeathLink(new DeathLink(source, cause));
                Plugin.Log.LogInfo("[AP] Sent DeathLink after the monarch died.");
            }
            catch (Exception ex)
            {
                Plugin.Log.LogError($"[AP] Could not send DeathLink: {ex.Message}");
            }
        }

        public static void SocketClosed(string reason)
        {
            Console.WriteLine("WS CLOSED");
            Console.WriteLine("Lost connection to Archipelago server. " + reason);
        }

        public static void ErrorReceived(Exception e, string message)
        {
            Console.WriteLine("WS ERRORED");
            Console.WriteLine(message);
            if (e != null) Console.WriteLine(e.ToString());
            //Disconnect();
        }

        private static async void OnPacktRevieved(ArchipelagoPacketBase packet)
        {
            Plugin.Log.LogInfo(packet.ToJObject().ToString());
        }

        private static void OnItemReceived(ReceivedItemsHelper helper)
        {
            while (helper.PeekItem() is { } item)
            {
                Plugin.Log.LogInfo($"[AP] Received item {item.ItemId}: {item.ItemGame} from {item.Player}");
                PendingItems.Enqueue(item.ItemId);
                helper.DequeueItem();
            }
        }

        public static void ProcessPendingItems()
        {
            if (!Plugin.APconnected) return;

            while (PendingItems.TryPeek(out long itemId))
            {
                if (!Plugin.ApplyReceivedItem(itemId))
                    return;

                PendingItems.TryDequeue(out _);
            }
        }

        public static void ProcessPendingDeathLinks()
        {
            if (PendingDeathLinks.IsEmpty || Plugin.AP?.Connected != true) return;
            while (PendingDeathLinks.TryDequeue(out var deathLink))
                Plugin.ApplyIncomingDeathLink(deathLink);
        }

        public void CompleteLocation(long locationId)
        {
            if (!Connected) return;

            Plugin.Log.LogInfo($"[AP] Completed location {locationId}");
            Session.Locations.CompleteLocationChecks(locationId);
        }
    }
}

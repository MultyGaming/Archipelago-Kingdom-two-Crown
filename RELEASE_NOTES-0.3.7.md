# Archipelago Kingdom Two Crowns — 0.3.7

## Mod plugin 0.3.7

- Coin and gem chest checks trigger when the chest has finished opening and spilling its contents, and progressive checks use the local/server check ledger to avoid repeats.
- Portal destruction checks wait for the island scene to remain active, so leaving by boat does not count as destroying a portal.
- Checks are saved locally per Archipelago seed and slot, then merged with the server's checked locations on reconnect.
- Resident counts include peasants only from the current island scene; milestone thresholds use the highest island peak rather than summing separate islands.
- Stone and iron technology availability is enforced after the game's `Kingdom.Update` logic runs.

## APWorld 0.3.3

- Filler is now named **Single Gold Coin** and still awards one coin.
- The Norselands wolf location is named **Norselands Island 6 Wolf Unlocks** and requires the Island 5 Liberation check to be logically reachable.
- The item/location ID remains unchanged for the renamed checks/items. Generate a new seed with APWorld 0.3.3 so the new names and logic are used.

## Feedback requiring in-game confirmation

- Verify chest checks on all islands and both chest types.
- Verify stone upgrades remain blocked until the Stone Technology item is received.
- Verify boat departure does not generate a portal check, while a real portal destruction does.
- Verify the Norselands Island 6 blue wolf mount triggers its renamed location.

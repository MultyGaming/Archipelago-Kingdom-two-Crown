# Kingdom Two Crowns — Archipelago

This project continues the [original Archipelago mod by Catalyss](https://github.com/Catalyss/Archipelago-Kingdom2Crown), created for an earlier Kingdom Two Crowns version. This version has been updated for Kingdom Two Crowns 2.4.3 with the assistance of AI (ChatGPT/Codex). Everyone is welcome to reuse, fork, and adapt the project; please retain applicable third-party notices and follow the licenses of its dependencies.

Archipelago integration for **Kingdom Two Crowns**.

## Compatibility target

- Kingdom Two Crowns **2.4.3**, Windows x64
- Archipelago **0.6.8** (minimum version required by this APWorld)
- Mod plugin **0.3.5**
- APWorld **0.3.2**
- BepInEx **6.0.0-be.753**, Unity IL2CPP, Windows x64

The tested base is BepInEx **6.0.0-be.753**. In our test installation, the game did not start with only the official files from that build. `PatchAK2C.zip` therefore provides the `core` and `patchers` folders from the working modpack setup; copying them over the corresponding game folders allows the game to start in that setup. This is not a standalone BepInEx installation: install the official `.753` archive first.

## Files in this repository

- `BepInEx/plugins/ArchipelagoRandomizer/` — mod plugin and its required DLL dependencies.
- `PatchAK2C.zip` — `core` and `patchers` files to copy into the game's `BepInEx` folder, replacing existing files.
- `kingdomtwocrowns.apworld` — packaged Archipelago world for local generation.
- `worlds/kingdomtwocrowns/` — APWorld source.
- `src/Mod/` — BepInEx plugin source.

## Install BepInEx

Download the exact **Unity IL2CPP, Windows x64, build 753** archive:

[`BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.753+0d275a4.zip`](https://builds.bepinex.dev/projects/bepinex_be/753/BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.753%2B0d275a4.zip)

Extract its contents into the game folder containing `KingdomTwoCrowns.exe`. The official [BepInEx IL2CPP installation guide](https://docs.bepinex.dev/master/articles/user_guide/installation/unity_il2cpp.html) explains the base installation. The official archive provides the BepInEx base; `PatchAK2C.zip` in this repository supplies the `core` and `patchers` folders used by the tested setup.

## Install the mod

1. Extract BepInEx `.753` into the game folder containing `KingdomTwoCrowns.exe`.
2. Close the game if it is running. Extract `PatchAK2C.zip` to a temporary folder, then copy its `core` and `patchers` folders into the game's `BepInEx` folder. Allow existing files to be replaced. The destinations are `BepInEx/core` and `BepInEx/patchers`; the zip does not contain the parent `BepInEx` folder.
3. Copy this repository's `BepInEx/plugins/ArchipelagoRandomizer` folder into the game's `BepInEx/plugins` folder.
4. To generate a local Archipelago game, install `kingdomtwocrowns.apworld` in the Archipelago Launcher with **Install APWorld**. You can also double-click the `.apworld` file. See the [Archipelago setup guide](https://archipelago.gg/tutorial/Archipelago/setup_en#playing-with-custom-worlds). The `.apworld` is needed by the generator; the mod DLLs are needed in the game.
5. Launch the game, enter the server address and port, slot name, and optional password in the in-game connection panel, then load the generated seed. The DeathLink mode is selected in the generated YAML.

## DeathLink

Choose one mode in the YAML: **Disabled**, **DeathLink** (drop all carried coins when a linked player dies), **DeathLink Hard** (lose the crown), or **DeathLink Extreme** (take fatal damage). When DeathLink is enabled, an actual local monarch death is also sent to Archipelago. The connection panel does not override the YAML selection.

BepInEx generates the game's IL2CPP interop files on first launch. Do not copy `interop`, logs, cache, or personal config files from another installation.

## Build from source

Install the .NET 6 SDK, BepInEx 6.0.0-be.753, and run the game once so BepInEx generates `BepInEx/interop`. Then build:

```powershell
dotnet build src/Mod/APKingdom2Crown.csproj -c Release -p:GameDir="C:\Program Files (x86)\Steam\steamapps\common\Kingdom Two Crowns"
```

`GameDir` can point to a different game installation. The project uses the generated interop assemblies and BepInEx core from that installation.

## Logs and troubleshooting

After launching, check `BepInEx/LogOutput.log`. When reporting a problem, include that log, the game version, the BepInEx version, and the Archipelago server version. Do not include save files or credentials.

## Third-party components

BepInEx is a separate project distributed under LGPL-2.1. `PatchAK2C.zip` redistributes BepInEx `core` files and a configuration-manager patcher from the tested modpack setup; install the official `.753` base first. Included dependency DLLs retain their respective upstream terms; see [THIRD_PARTY.md](THIRD_PARTY.md).

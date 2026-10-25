# Kingdom Two Crowns — Archipelago

This project continues the [original Archipelago mod by Catalyss](https://github.com/Catalyss/Archipelago-Kingdom2Crown), created for an earlier Kingdom Two Crowns version. This version has been updated for Kingdom Two Crowns 2.4.3 with the assistance of AI (ChatGPT/Codex). Everyone is welcome to reuse, fork, and adapt the project; please retain applicable third-party notices and follow the licenses of its dependencies.

Archipelago integration for **Kingdom Two Crowns**.

## Tested setup

- Kingdom Two Crowns **2.4.3**, Windows x64
- Archipelago **0.6.8** (minimum version required by this APWorld)
- Mod plugin **0.3.2**
- APWorld **0.3.1**
- BepInEx **6.0.0-be.753**, Unity IL2CPP, Windows x64

The BepInEx version is pinned to the build tested with the game. Its IL2CPP loader, preloader and patching support come in the official BepInEx archive; no separate IL2CPP patcher is required. The optional BepInEx Configuration Manager patcher is not required by this mod.

## Files in this repository

- `BepInEx/plugins/ArchipelagoRandomizer/` — mod plugin and its required DLL dependencies.
- `kingdomtwocrowns.apworld` — packaged Archipelago world for local generation.
- `worlds/kingdomtwocrowns/` — APWorld source.
- `src/Mod/` — BepInEx plugin source.

## Install BepInEx

Download the exact **Unity IL2CPP, Windows x64, build 753** archive:

[`BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.753+0d275a4.zip`](https://builds.bepinex.dev/projects/bepinex_be/753/BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.753%2B0d275a4.zip)

Extract its contents into the game folder containing `KingdomTwoCrowns.exe`. The official [BepInEx IL2CPP installation guide](https://docs.bepinex.dev/master/articles/user_guide/installation/unity_il2cpp.html) explains the first launch and generated files. The BepInEx build is an external dependency and is not bundled here.

## Install the mod

1. Extract BepInEx into the game folder and launch the game once so it can generate its IL2CPP files. Close the game when it reaches the menu.
2. Copy this repository's `BepInEx/plugins/ArchipelagoRandomizer` folder into the game's `BepInEx/plugins` folder.
3. To generate a local Archipelago game, install `kingdomtwocrowns.apworld` in the Archipelago Launcher with **Install APWorld**. You can also double-click the `.apworld` file. See the [Archipelago setup guide](https://archipelago.gg/tutorial/Archipelago/setup_en#playing-with-custom-worlds). The `.apworld` is needed by the generator; the mod DLLs are needed in the game.
4. Launch the game, connect to the Archipelago server from the mod's in-game connection panel, and load the generated seed.

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

BepInEx is a separate project distributed under LGPL-2.1. This repository does not bundle or modify its runtime; download it from the official BepInEx build service. The included mod dependency DLLs retain their respective upstream terms.

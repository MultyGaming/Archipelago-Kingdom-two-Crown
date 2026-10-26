# Kingdom Two Crowns — Archipelago

Ce projet poursuit le [mod Archipelago original de Catalyss](https://github.com/Catalyss/Archipelago-Kingdom2Crown), créé pour une ancienne version de Kingdom Two Crowns. Cette version a été mise à jour pour Kingdom Two Crowns 2.4.3 avec l’aide de l’IA (ChatGPT/Codex). Chacun peut reprendre, forker et adapter le projet ; merci de conserver les mentions des composants tiers et de respecter les licences de ses dépendances.

Intégration Archipelago pour **Kingdom Two Crowns**.

## Compatibilité visée

- Kingdom Two Crowns **2.4.3**, Windows x64
- Archipelago **0.6.8** (version minimale requise par cet APWorld)
- Plugin du mod **0.3.5**
- APWorld **0.3.2**
- BepInEx **6.0.0-be.753**, Unity IL2CPP, Windows x64

La version de base testée est BepInEx **6.0.0-be.753**. Le jeu ne démarrait pas avec le seul contenu officiel de cette version dans notre installation de test. `PatchAK2C.zip` fournit donc un ensemble `core` et `patchers` issu du modpack fonctionnel, qui remplace les fichiers correspondants et permet au jeu de démarrer dans cette configuration. Ce zip n’est pas une installation BepInEx autonome : installe d’abord l’archive officielle `.753`.

## Contenu du dépôt

- `BepInEx/plugins/ArchipelagoRandomizer/` — plugin du mod et DLL dont il dépend.
- `PatchAK2C.zip` — fichiers `core` et `patchers` à copier dans le dossier `BepInEx` du jeu en remplaçant les fichiers existants.
- `kingdomtwocrowns.apworld` — monde Archipelago à installer pour générer une partie en local.
- `worlds/kingdomtwocrowns/` — sources de l’APWorld.
- `src/Mod/` — sources du plugin BepInEx.

## Installer BepInEx

Télécharge l’archive exacte **Unity IL2CPP, Windows x64, build 753** :

[`BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.753+0d275a4.zip`](https://builds.bepinex.dev/projects/bepinex_be/753/BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.753%2B0d275a4.zip)

Décompresse son contenu dans le dossier du jeu où se trouve `KingdomTwoCrowns.exe`. Le [guide officiel d’installation IL2CPP de BepInEx](https://docs.bepinex.dev/master/articles/user_guide/installation/unity_il2cpp.html) décrit l’installation de base. L’archive officielle fournit la base BepInEx ; `PatchAK2C.zip` dans ce dépôt apporte les dossiers `core` et `patchers` nécessaires à la configuration testée ici.

## Installer le mod

1. Décompresse BepInEx `.753` dans le dossier du jeu où se trouve `KingdomTwoCrowns.exe`.
2. Ferme le jeu s’il est ouvert. Décompresse `PatchAK2C.zip` dans un dossier temporaire, puis copie ses dossiers `core` et `patchers` dans le dossier `BepInEx` du jeu. Accepte le remplacement des fichiers existants. Les destinations sont `BepInEx/core` et `BepInEx/patchers`. Le zip ne contient pas les dossiers `BepInEx` englobants.
3. Copie le dossier `BepInEx/plugins/ArchipelagoRandomizer` de ce dépôt dans le dossier `BepInEx/plugins` du jeu.
4. Pour générer une partie Archipelago en local, installe `kingdomtwocrowns.apworld` dans l’Archipelago Launcher avec **Install APWorld**. Tu peux aussi double-cliquer sur le fichier `.apworld`. Consulte le [guide de configuration Archipelago](https://archipelago.gg/tutorial/Archipelago/setup_en#playing-with-custom-worlds). Le fichier `.apworld` sert au générateur ; les DLL du mod doivent être dans le jeu.
5. Lance le jeu, saisis l’adresse et le port du serveur, le nom du slot et le mot de passe éventuel dans le panneau de connexion, puis charge la graine générée. Le mode DeathLink se choisit dans le YAML généré.

## DeathLink

Choisis un mode dans le YAML : **Désactivé**, **DeathLink** (perdre toutes les pièces transportées quand un joueur lié meurt), **DeathLink Hard** (perdre la couronne) ou **DeathLink Extreme** (subir des dégâts mortels). Si DeathLink est activé, la mort réelle du monarque local est également signalée à Archipelago. Le panneau de connexion ne remplace pas le choix du YAML.

BepInEx crée les fichiers d’interop IL2CPP du jeu lors du premier lancement. Ne copie pas les dossiers `interop`, les journaux, le cache ou les fichiers de configuration personnels d’une autre installation.

## Compiler les sources

Installe le SDK .NET 6 et BepInEx 6.0.0-be.753, puis lance le jeu une fois afin que BepInEx génère `BepInEx/interop`. Compile ensuite le projet :

```powershell
dotnet build src/Mod/APKingdom2Crown.csproj -c Release -p:GameDir="C:\Program Files (x86)\Steam\steamapps\common\Kingdom Two Crowns"
```

`GameDir` peut désigner un autre emplacement du jeu. Le projet utilise les assemblages interop générés et les fichiers core de BepInEx présents dans cette installation.

## Journaux et dépannage

Après le lancement, consulte `BepInEx/LogOutput.log`. Pour signaler un problème, joins ce journal et indique la version du jeu, de BepInEx et du serveur Archipelago. N’envoie pas de sauvegarde ni de mot de passe.

## Composants tiers

BepInEx est un projet séparé distribué sous licence LGPL-2.1. `PatchAK2C.zip` redistribue les fichiers BepInEx `core` et le patcher de gestionnaire de configuration provenant du modpack de test ; installe d’abord la base officielle `.753`. Les DLL de dépendances incluses conservent leurs licences respectives ; voir [THIRD_PARTY.md](THIRD_PARTY.md).

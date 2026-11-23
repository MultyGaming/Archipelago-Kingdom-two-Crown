# Release notes / Notes de version

## English

Generate a new game to use the updated names and logic.

### Mod plugin

- Coin and gem chest checks complete when the chest finishes opening.
- Checks are saved locally per Archipelago seed and slot. Checks already recorded locally or confirmed by the server are not resent after reconnecting.
- Leaving by boat does not count as destroying a portal.
- Resident checks count peasants on the current island only; population milestones use the highest island peak instead of adding peaks across islands.
- Stone and iron technology restrictions are applied after the game's update logic.
- Each mount unlock check is sent by that individual mount's payment hook after it is purchased with gems.

### Archipelago world

- “Single Gold Coin” filler awards one coin.
- “Norselands Island 6 Wolf Unlocks” checks the Blue Wolf purchase on Norselands island 6. Island 5 Liberation is not required for this check.
- IDs for renamed items and locations remain unchanged.

## Français

Il faut générer une nouvelle partie pour prendre en compte les noms et la logique mis à jour.

### Plugin du mod

- Les checks des coffres de pièces et de gemmes sont validés quand l’ouverture du coffre est terminée.
- Les checks sont sauvegardés localement par graine et slot Archipelago. Ceux déjà enregistrés localement ou confirmés par le serveur ne sont pas renvoyés après reconnexion.
- Un départ en bateau ne compte pas comme une destruction de portail.
- Les checks d’habitants comptent les paysans de l’île actuelle uniquement ; les seuils utilisent le pic le plus élevé d’une île au lieu d’additionner les pics de plusieurs îles.
- Les restrictions des technologies de pierre et de fer sont appliquées après la logique de mise à jour du jeu.
- Le check de chaque monture est envoyé par le hook de paiement de cette monture, après son achat avec des gemmes.

### Monde Archipelago

- Le filler « Single Gold Coin » donne une pièce.
- « Norselands Island 6 Wolf Unlocks » vérifie l’achat du Blue Wolf sur l’île 6 de Norselands. La libération de l’île 5 n’est pas requise pour ce check.
- Les identifiants des objets et localisations renommés restent inchangés.

from BaseClasses import Location

class KTCLocation(Location):
    game: str = "Kingdom Two Crowns"


# IDs 755180-755270 are reserved for the nine optional milestone families.
# Keep this order synchronized with APCheckTracker.MilestoneFamilies in the mod.
MILESTONES = {
    "Residents": [5, 10, 15, 20, 30, 40, 50, 65, 80, 95, 100, 115, 135, 150],
    "Archers": [5, 10, 15, 20, 30, 40, 50, 65, 80, 95, 100, 115, 135, 150],
    "Workers": [5, 10, 15, 20, 30, 40, 50, 65, 80, 95, 100, 115, 135, 150],
    "Basic Knights": [1, 2, 4, 8, 12, 20],
    "Iron Knights": [1, 2, 4, 8, 12, 20],
    "Farmers": [5, 10, 15, 20, 30, 40, 50, 65, 75],
    "Pikemen": [5, 10, 15, 20, 30, 40, 50, 65, 75],
    "Catapults": [1, 2, 4, 6, 10],
    "Treasury": [5, 10, 15, 20, 30, 40, 50, 65, 80, 95, 100, 115, 135, 150],
}

location_table = {
    # Progressive Portals
    **{f"Destroy Portal Progressive {i}": 755066 + i for i in range(1, 24)},

    # Hermit Unlock
    "Hermit Ballista Unlock": 755096,
    "Hermit Bakery Unlock": 755098,
    "Hermit Horn Unlock": 755100,
    "Hermit Stable Unlock": 755102,
    "Hermit Warrior Unlock": 755104,

    # Islands and their standard checks
    "Island 1 Liberation": 755106,
    "Progressive Coin Chest 1": 755107,
    "Progressive Coin Chest 2": 755108,
    "Progressive Coin Chest 3": 755109,
    "Island 2 Liberation": 755110,
    "Progressive Coin Chest 4": 755111,
    "Progressive Coin Chest 5": 755112,
    "Progressive Coin Gem 1": 755113,
    "Progressive Coin Gem 2": 755114,
    "Progressive Coin Gem 3": 755115,
    "Island 2 Dog": 755116,
    "Island 3 Liberation": 755117,
    "Progressive Coin Chest 6": 755118,
    "Progressive Coin Chest 7": 755119,
    "Progressive Coin Chest 8": 755120,
    "Progressive Coin Gem 4": 755121,
    "Progressive Coin Gem 5": 755122,
    "Progressive Coin Gem 6": 755123,
    "Island 4 Liberation": 755124,
    "Progressive Coin Chest 9": 755125,
    "Progressive Coin Gem 7": 755126,
    "Progressive Coin Gem 8": 755127,
    "Progressive Coin Gem 9": 755128,
    "Island 5 Liberation": 755129,
    "Progressive Coin Gem 10": 755130,
    "Progressive Coin Gem 11": 755131,
    "Progressive Coin Gem 12": 755132,

    # Mount Unlocks
    "Bear Unlocks": 755133,
    "Stag Unlocks": 755134,
    "Lizard Unlocks": 755135,
    "Unicorn Unlocks": 755136,
    "Wolf P1 Unlocks": 755137,
    "Warhorse P1 Unlocks": 755138,
    "Horse Fast Unlocks": 755139,
    "Griffin P1 Unlocks": 755140,
    "Griffin Skull P1 Unlocks": 755141,
    "Horse Stamina Unlocks": 755142,
    "Wolf_norselands Unlocks": 755143,
    "Reindeer Unlocks": 755144,
    "Horse Burst Unlocks": 755145,
    "Rainbow Pony Unlocks": 755146,
    "Warhorse Plague P1 Unlocks": 755147,
    "Wolf Norselands P1 Unlocks": 755148,
    "Unicorn Dark Unlocks": 755149,

    # Status Unlocks
    "Archery Unlocks": 755171,
    "Scythe Unlocks": 755172,
    "Building Unlocks": 755173,
    "Knights Unlocks": 755174,

    # One check per island for the first lighthouse tier
    **{f"Island {i} Lighthouse T1": 755279 + i for i in range(1, 6)},

    # The selected objective is tracked as one Archipelago event location.
    "Archipelago Goal": 755290,
}

_next_id = 755179
for family, thresholds in MILESTONES.items():
    for threshold in thresholds:
        _next_id += 1
        location_table[f"{family} {threshold}"] = _next_id
assert _next_id == 755270

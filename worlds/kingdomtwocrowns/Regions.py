from BaseClasses import MultiWorld, Region
from .Locations import KTCLocation, location_table, MILESTONES


MILESTONE_OPTIONS = {
    "Residents": "population_checks",
    "Archers": "archer_checks",
    "Workers": "worker_checks",
    "Basic Knights": "basic_knight_checks",
    "Iron Knights": "iron_knight_checks",
    "Farmers": "farmer_checks",
    "Pikemen": "pikeman_checks",
    "Catapults": "catapult_checks",
    "Treasury": "treasury_checks",
}


def create_regions(world: MultiWorld, player: int, ap_world=None):
    start = Region("Menu", player, world, "Kingdom Two Crowns")
    disabled = set()
    if ap_world is not None:
        for family, option_name in MILESTONE_OPTIONS.items():
            if not getattr(ap_world.options, option_name).value:
                disabled.update(f"{family} {threshold}" for threshold in MILESTONES[family])
        lighthouse_goal = ap_world.options.goal in (1, 3)
        if not ap_world.options.lighthouse_checks.value and not lighthouse_goal:
            disabled.update(f"Island {i} Lighthouse T1" for i in range(1, 6))

    start.locations += [
        KTCLocation(player, name, location_id, start)
        for name, location_id in location_table.items()
        if name not in disabled
    ]
    world.regions.append(start)

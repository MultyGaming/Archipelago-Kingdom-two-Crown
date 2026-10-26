from dataclasses import dataclass
from Options import PerGameCommonOptions, Range, Toggle, Choice


class PopulationChecks(Toggle):
    """Enable all resident population milestone checks."""
    display_name = "Resident Checks"
    default = 1

class ArcherChecks(Toggle):
    """Enable all archer milestone checks."""
    display_name = "Archer Checks"
    default = 1

class WorkerChecks(Toggle):
    """Enable all worker milestone checks."""
    display_name = "Worker Checks"
    default = 1

class BasicKnightChecks(Toggle):
    """Enable basic knight milestone checks."""
    display_name = "Basic Knight Checks"
    default = 1

class IronKnightChecks(Toggle):
    """Enable iron-upgraded knight milestone checks."""
    display_name = "Iron Knight Checks"
    default = 1

class FarmerChecks(Toggle):
    """Enable all farmer milestone checks."""
    display_name = "Farmer Checks"
    default = 1

class PikemanChecks(Toggle):
    """Enable all pikeman milestone checks."""
    display_name = "Pikeman Checks"
    default = 1

class CatapultChecks(Toggle):
    """Enable all catapult milestone checks."""
    display_name = "Catapult Checks"
    default = 1

class TreasuryChecks(Toggle):
    """Enable all castle treasury milestone checks."""
    display_name = "Castle Treasury Checks"
    default = 1

class LighthouseChecks(Toggle):
    """Enable the per-island first lighthouse tier checks."""
    display_name = "Lighthouse Checks"
    default = 1

class Goal(Choice):
    """Select the in-game condition that completes this Archipelago slot."""
    display_name = "Goal"
    option_liberate_all_islands = 0
    option_build_all_lighthouses = 1
    option_liberate_islands = 2
    option_build_lighthouses = 3
    option_destroy_small_portals = 4
    default = 0

class GoalIslandCount(Range):
    """Island count for custom liberation or lighthouse goals."""
    display_name = "Custom Goal Island Count"
    range_start = 1
    range_end = 5
    default = 5

class GoalPortalCount(Range):
    """Number of small (non-cliff) portals to destroy for the custom portal goal."""
    display_name = "Custom Goal Small Portal Count"
    range_start = 1
    range_end = 23
    default = 23

class DeathLinkMode(Choice):
    """Choose what happens when another DeathLink player dies. Local deaths always send a DeathLink when enabled."""
    display_name = "DeathLink Mode"
    option_disabled = 0
    option_deathlink = 1
    option_deathlink_hard = 2
    option_deathlink_extreme = 3
    default = 0

class GoldPouchCount(Range):
    """Number of random 5-10 coin rewards in the item pool."""
    display_name = "Gold Pouches in Item Pool"
    range_start = 0
    range_end = 34
    default = 10

class GemPackCount(Range):
    """Number of rare random 1-3 gem rewards in the item pool."""
    display_name = "Gem Packs in Item Pool (Rare)"
    range_start = 0
    range_end = 5
    default = 1

@dataclass
class KingdomTwoCrownsOptions(PerGameCommonOptions):
    population_checks: PopulationChecks
    archer_checks: ArcherChecks
    worker_checks: WorkerChecks
    basic_knight_checks: BasicKnightChecks
    iron_knight_checks: IronKnightChecks
    farmer_checks: FarmerChecks
    pikeman_checks: PikemanChecks
    catapult_checks: CatapultChecks
    treasury_checks: TreasuryChecks
    lighthouse_checks: LighthouseChecks
    goal: Goal
    goal_island_count: GoalIslandCount
    goal_portal_count: GoalPortalCount
    deathlink_mode: DeathLinkMode
    gold_pouch_count: GoldPouchCount
    gem_pack_count: GemPackCount

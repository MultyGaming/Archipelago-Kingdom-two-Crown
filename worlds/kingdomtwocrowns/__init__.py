from typing import NamedTuple, Union
import logging

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import set_rule
from NetUtils import SlotType

from .Items import item_table, KTCItem
from .Locations import location_table, KTCLocation, MILESTONES
from .Regions import create_regions, MILESTONE_OPTIONS
from .Options import KingdomTwoCrownsOptions, Goal


class KingdomTwoCrownsWeb(WebWorld):
    pass


class KingdomTwoCrownsWorld(World):
    game = "Kingdom Two Crowns"
    topology_present = True
    item_name_to_id = item_table
    location_name_to_id = location_table
    web = KingdomTwoCrownsWeb()
    options_dataclass = KingdomTwoCrownsOptions
    options: KingdomTwoCrownsOptions

    def create_regions(self):
        create_regions(self.multiworld, self.player, self)

    def set_rules(self):
        mw, p = self.multiworld, self.player

        island1 = [
            "Island 1 Liberation", "Archery Unlocks", "Griffin P1 Unlocks", "Hermit Ballista Unlock",
            "Progressive Coin Chest 1", "Progressive Coin Chest 2", "Progressive Coin Chest 3",
        ]
        island2 = [
            "Scythe Unlocks", "Stag Unlocks", "Hermit Stable Unlock", "Island 2 Dog",
            "Island 2 Liberation", "Progressive Coin Chest 4", "Progressive Coin Chest 5",
            "Progressive Coin Gem 1", "Progressive Coin Gem 2", "Progressive Coin Gem 3",
        ]
        island3 = [
            "Building Unlocks", "Warhorse P1 Unlocks", "Hermit Bakery Unlock", "Island 3 Liberation",
            "Progressive Coin Chest 6", "Progressive Coin Chest 7", "Progressive Coin Chest 8",
            "Progressive Coin Gem 4", "Progressive Coin Gem 5", "Progressive Coin Gem 6",
        ]
        island4 = [
            "Island 4 Liberation", "Progressive Coin Chest 9", "Progressive Coin Gem 7",
            "Progressive Coin Gem 8", "Progressive Coin Gem 9", "Bear Unlocks", "Lizard Unlocks",
            "Hermit Warrior Unlock",
        ]
        island5 = [
            "Island 5 Liberation", "Progressive Coin Gem 10", "Progressive Coin Gem 11",
            "Progressive Coin Gem 12", "Unicorn Unlocks", "Knights Unlocks", "Hermit Horn Unlock",
        ]

        for name in island1:
            set_rule(mw.get_location(name, p), lambda state: True)
        for name in island2:
            set_rule(mw.get_location(name, p), lambda state: has_tiers(state, p, 3))
        for name in island3:
            set_rule(mw.get_location(name, p), lambda state: has_stone_tier(state, p, 4))
        for name in island4:
            set_rule(mw.get_location(name, p), lambda state: has_stone_tier(state, p, 6))
        for name in island5:
            set_rule(mw.get_location(name, p), lambda state: has_iron_tier(state, p, 7))

        if self.options.lighthouse_checks.value or self.options.goal in (
                Goal.option_build_all_lighthouses, Goal.option_build_lighthouses):
            for island in range(1, 6):
                liberation_name = f"Island {island} Liberation"
                set_rule(mw.get_location(f"Island {island} Lighthouse T1", p),
                         lambda state, name=liberation_name: state.can_reach(mw.get_location(name, p)))

        for family, thresholds in MILESTONES.items():
            option_name = MILESTONE_OPTIONS[family]
            if not getattr(self.options, option_name).value:
                continue
            for threshold in thresholds:
                location = mw.get_location(f"{family} {threshold}", p)
                set_rule(location, lambda state, f=family, t=threshold: milestone_rule(state, p, f, t))

        # Base check for reaching each small/non-cliff portal; progression is still tier-gated.
        for tier in range(1, 24):
            set_rule(mw.get_location(f"Destroy Portal Progressive {tier}", p),
                     lambda state, t=tier: self.portal_rule(state, p, t))

        for name in ["Archipelago Goal"]:
            set_rule(mw.get_location(name, p), lambda state: self.goal_rule(state, p))

    def portal_rule(self, state, player, tier):
        if tier < 5:
            return has_stone_tier(state, player, 4)
        if tier < 9:
            return has_stone_tier(state, player, 5)
        return has_iron_tier(state, player, 7)

    def goal_rule(self, state, player):
        goal = self.options.goal.value
        island_locations = [self.multiworld.get_location(f"Island {i} Liberation", player) for i in range(1, 6)]
        if goal == Goal.option_liberate_all_islands:
            return all(state.can_reach(location) for location in island_locations)
        if goal == Goal.option_liberate_islands:
            return sum(state.can_reach(location) for location in island_locations) >= self.options.goal_island_count.value
        if goal == Goal.option_build_all_lighthouses:
            lighthouse_locations = [self.multiworld.get_location(f"Island {i} Lighthouse T1", player)
                                    for i in range(1, 6)]
            return all(state.can_reach(location) for location in lighthouse_locations)
        if goal == Goal.option_build_lighthouses:
            required_islands = self.options.goal_island_count.value
            lighthouse_locations = [self.multiworld.get_location(f"Island {i} Lighthouse T1", player)
                                    for i in range(1, 6)]
            lighthouse_access = [state.can_reach(location) for location in lighthouse_locations]
            return sum(lighthouse_access) >= required_islands
        if goal == Goal.option_destroy_small_portals:
            return state.can_reach(
                self.multiworld.get_location(f"Destroy Portal Progressive {self.options.goal_portal_count.value}", player)
            )
        return False

    def generate_early(self):
        if self.options.goal in (Goal.option_build_all_lighthouses, Goal.option_build_lighthouses) \
                and not self.options.lighthouse_checks.value:
            raise ValueError("Lighthouse goals require Lighthouse Checks to be enabled.")
        self.multiworld.player_types[self.player] = SlotType.player

    def fill_slot_data(self):
        data = {
            "goal": self.options.goal.value,
            "goal_island_count": self.options.goal_island_count.value,
            "goal_portal_count": self.options.goal_portal_count.value,
            "deathlink_mode": self.options.deathlink_mode.value,
            "lighthouse_checks": self.options.lighthouse_checks.value,
            "gold_pouch_count": self.options.gold_pouch_count.value,
            "gem_pack_count": self.options.gem_pack_count.value,
        }
        data.update({f"{option_name}": getattr(self.options, option_name).value
                     for option_name in MILESTONE_OPTIONS.values()})
        return data

    def pre_fill(self):
        goal_location = self.multiworld.get_location("Archipelago Goal", self.player)
        goal_location.place_locked_item(
            KTCItem("Victory", ItemClassification.progression, item_table["Victory"], self.player)
        )
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_item(self, name: str, classification: ItemClassification = ItemClassification.filler) -> Item:
        return KTCItem(name, classification, item_table[name], self.player)

    def get_filler_item_name(self) -> str:
        return "Gold Coin"

    def create_items(self):
        progression_items = {
            "Progressive Castle Unlock T1", "Progressive Castle Unlock T2", "Progressive Castle Unlock T3",
            "Stone Technology", "Progressive Castle Unlock T4", "Progressive Castle Unlock T5",
            "Progressive Castle Unlock T6", "Iron Technology", "Progressive Castle Unlock T7",
        }
        currency_items = {"Gold Pouch", "Gem Pack", "Victory"}
        items = [self.create_item(name, ItemClassification.progression) for name in progression_items]
        excluded_items = progression_items | currency_items | {"Random Game Effect (junk)"}
        items += [self.create_item(name) for name in item_table if name not in excluded_items]
        items += [self.create_item("Gold Pouch") for _ in range(self.options.gold_pouch_count.value)]
        items += [self.create_item("Gem Pack", ItemClassification.useful)
                  for _ in range(self.options.gem_pack_count.value)]

        missing_items = len(self.multiworld.get_locations(self.player)) - 1 - len(items)
        if missing_items < 0:
            raise ValueError("The selected currency item counts exceed the available locations.")
        items += [self.create_item("Gold Coin") for _ in range(missing_items)]
        self.multiworld.itempool += items


def has_tiers(state, player, last_tier):
    return all(state.has(f"Progressive Castle Unlock T{tier}", player) for tier in range(1, last_tier + 1))


def has_stone_tier(state, player, last_tier):
    return state.has("Stone Technology", player) and has_tiers(state, player, last_tier)


def has_iron_tier(state, player, last_tier):
    return state.has("Iron Technology", player) and has_tiers(state, player, last_tier)


def milestone_rule(state, player, family, threshold):
    if family in {"Basic Knights", "Catapults", "Pikemen"}:
        return has_stone_tier(state, player, 5)
    if family == "Iron Knights":
        return has_iron_tier(state, player, 7)
    if family == "Farmers":
        return has_tiers(state, player, 3) and (threshold < 50 or has_tiers(state, player, 4))
    if family == "Treasury":
        return has_tiers(state, player, 4) and (threshold < 80 or has_stone_tier(state, player, 5))
    if threshold <= 20:
        return True
    if threshold <= 50:
        return has_tiers(state, player, 3)
    if threshold <= 95:
        return has_stone_tier(state, player, 5)
    return has_iron_tier(state, player, 7)


class PlandoItem(NamedTuple):
    item: str
    location: str
    world: Union[bool, str] = False
    from_pool: bool = True
    force: str = 'silent'

    def warn(self, warning: str):
        if self.force in {'true', 'fail', 'failure', 'none', 'false', 'warn', 'warning'}:
            logging.warning(warning)
        else:
            logging.debug(warning)

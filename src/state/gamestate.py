from src.entities.npc import NPC
from src.quests.quest_log import QuestLog
from src.travel.location import Location

from enum import Enum


class CurrentActivity(Enum):
    TRAVELLING = "TRAVELLING"
    IDLE = "IDLE"
    FIGHTING = "FIGHTING"
    TALKING = "TALKING"


class GameState:
    def __init__(self):
        self.activity = CurrentActivity.TRAVELLING

        self.player: NPC = self.init_player()

        self.quest_log: QuestLog = self.init_quest_log()

        self.current_location: Location = None  # type: ignore
        self.current_fight = None
        self.set_location("location_bar")


    def game_loop(self) -> None:
        from src.travel.travel_dialogue import TravelDialogue
        while True:
            if self.activity == CurrentActivity.TRAVELLING or True:
                td = TravelDialogue()
                td.main_dialogue()


    def init_quest_log(self) -> QuestLog:
        quest_log = QuestLog()

        return quest_log

    def init_player(self) -> NPC:
        from src.data_providers import item_provider as ip

        player = NPC(name="Mary Sue", pronouns="3rd_she", hp_max=30, species="spec_human")

        inv = player.inventory

        dagger = ip["default_dagger"]
        tome = ip["default_pyro_tome"]
        mace = ip["default_mace"]
        chest = ip["leather_chest"]
        head = ip["leather_cap"]
        legs = ip["leather_pants"]

        inv.add(dagger)
        inv.add(tome)
        inv.add(mace)
        inv.add(chest)
        inv.add(head)
        inv.add(legs)

        return player

    def get_quest_log(self) -> QuestLog:
        return self.quest_log

    def get_player(self) -> NPC:
        return self.player

    def set_location(self, location_id: str):
        from src.data_providers import location_provider as lp
        self.current_location = lp[location_id]

    def start_monster_fight(self, monster_id) -> None:
        from src.data_providers import monster_provider as mp
        from src.combat.player_combat import PlayerCombat, PlayerCombatant
        from src.combat.monster_combatant import MonsterCombatant

        player_combatant = PlayerCombatant(self.player)
        monster = mp[monster_id]
        monster_combatant = MonsterCombatant(monster)

        player_combat = PlayerCombat(player_combatant, monster_combatant)
        self.activity = CurrentActivity.FIGHTING
        player_combat.combat()



global_state = GameState()

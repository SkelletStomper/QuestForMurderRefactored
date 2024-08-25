from src.entities.npc import NPC
from src.quests.quest_log import QuestLog


class GameState:
    def __init__(self):

        self.player: NPC = self.init_player()

        self.quest_log: QuestLog = self.init_quest_log()

    def init_quest_log(self) -> QuestLog:
        quest_log = QuestLog()

        return quest_log


    def init_player(self) -> NPC:
        from src.data_providers import item_provider as ip

        player = NPC(name="Mary Sue", pronouns="3rd_she", hp_max=30, species="spec_feline")

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
from src.combat.combat_basics import Attack
from src.combat.npc_combatant import NPCCombatant
from src.items.inventory_dialogue import InventoryDialogue
from src.entities.npc import NPC


from enum import Enum
from typing import Any
import logging
logger = logging.getLogger(__name__)


class PlayerCombatChoice(Enum):
    ATTACKING = "ATTACK"
    FLEEING = "FLEEING"
    INT_ACTION = "INT_ACTION"


class PlayerCombatant(NPCCombatant):
    def __init__(self, npc: NPC):
        super().__init__(npc)

    def turn(self) -> tuple[PlayerCombatChoice, Any]:
        while True:
            print("What do you want to do?")
            print("(1): Attack")
            print("(2): Inventory")
            print("(3): Flee")
            choice: str = input(">: ").lower()
            if choice in ["1", "(1)", "atk", "attack"]:
                attacks = self.attack_dialogue()
                if attacks is not None:
                    return PlayerCombatChoice.ATTACKING, attacks
            elif choice in ["2", "(2)", "inv", "inventory"]:
                took_turn = InventoryDialogue(self.npc.inventory, timed=True).dialogue()
                if took_turn:
                    return PlayerCombatChoice.INT_ACTION, None
            elif choice in ["3", "{3}", "flee", "run"]:
                return PlayerCombatChoice.FLEEING, None
            else:
                print("Please make a valid choice.")

    def attack_dialogue(self) -> list[tuple[Attack, int]] | None:
        equip_effects = self.npc.inventory.calculate_bonus()
        stencils = equip_effects.granted_attacks
        player_input = ""
        while player_input != "0":
            for i in range(0, len(stencils)):
                print(f"({i+1}): {stencils[i].name}")

            print("(0): Back")
            player_input = input(">:")
            index = int(player_input)-1
            if 0 <= index < len(stencils):
                return stencils[index].generate_attack()

        return None

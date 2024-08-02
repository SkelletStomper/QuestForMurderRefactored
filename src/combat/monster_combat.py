from src.combat.attack import Attack
from src.combat.monster_combatant import MonsterCombatant


class MonsterCombat:
    def __init__(self, combatant1: MonsterCombatant, combatant2: MonsterCombatant) -> None:
        self.combatant1 = combatant1
        self.combatant2 = combatant2

    def combat(self) -> None:
        c1 = self.combatant1
        c2 = self.combatant2

        while c1.is_alive and c2.is_alive:
            self.calculate_attacks(c1, c2)
            print("")

            self.calculate_attacks(c2, c1)
            print("")

    def calculate_attacks(self, attacker: MonsterCombatant, defender: MonsterCombatant) -> None:
        for attack in attacker.get_attacks():
            if defender.defense(attack):
                self.print_attack(attack, attacker, defender)
            if not defender.is_alive:
                continue
        defender.status_message()

    @staticmethod
    def print_attack(attack: Attack, attacker: MonsterCombatant, defender: MonsterCombatant) -> None:
        atk_str = attack.atk_str.parse(
            attacking=attacker.monster.get_le(),
            defending=defender.monster.get_le()
        )
        print(atk_str)

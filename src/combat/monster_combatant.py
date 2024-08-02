from src.combat.combat_basics import Combatant, attack_dodged
from src.combat.attack import Attack
from src.entities.monster import Monster
from src.localization.l_string import LString


class MonsterCombatant(Combatant):
    def __init__(self, monster: Monster) -> None:
        self.monster = monster
        self.hp = self.monster.hp_max

    def get_attacks(self) -> list[Attack]:
        le = self.monster.get_le()
        print(f"{le.name} attacks!".capitalize())

        dmg = self.monster.dmg
        text = LString("{atk.name} hits {def.name} with a vicious attack!")
        return [Attack(
            dmg=dmg,
            acc=self.monster.acc,
            crt=self.monster.crt,
            atk_str=text,

        )]

    def defense(self, attack: Attack) -> bool:
        """Let the monster defend against the Attack, giving it chance to dodge and applying damage if it.
        Returns true if the attack does damage, false if not."""

        le = self.monster.get_le()
        accuracy = attack.acc
        dodge = self.monster.dodge

        if attack_dodged(accuracy, dodge):
            print(f"{le.name} dodged the attack!".capitalize())
            return False

        dmg_factor = self.monster.calculate_dmg_factor(attack)
        dmg = round(attack.dmg*dmg_factor)
        dmg -= self.monster.armor

        if dmg > 0:
            dmg = round(dmg*attack.crt)
            self.hp -= dmg
            print(f"{le.name} got hit for {dmg} damage!".capitalize())
            return True
        else:
            print(f"The hit doesn't penetrate {le.owns} armor!")
            return False

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def status_message(self):
        le = self.monster.get_le()
        print(f"{le.name} has {self.hp} hit points left!".capitalize())


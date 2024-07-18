from monster import Monster

from attack import Attack, AttackType


class Combatant:
    def get_attacks(self) -> list[Attack]:
        # Abstract Method
        pass

    def defense(self, attack: Attack) -> None:
        # Abstract Method
        pass


    def is_alive(self) -> bool:
        # Abstract Method
        pass

class MonsterCombatant(Combatant):
    def __init__(self, monster: Monster) -> None:
        self.monster = monster
        self.hp = self.monster.hp_max

    def get_attacks(self) -> list[Attack]:
        print(f"{self.monster.title} {self.monster.name} attacks you!")
        dmg = round(self.monster.dmg * self.monster.crit_modifier)
        return [Attack(dmg)]

    def defense(self, attack: Attack) -> None:

        dmg_factor = self.monster.calculate_dmg_factor(attack)

        dmg = round(attack.dmg*dmg_factor)

        dmg -= self.monster.armor

        if dmg > 0:
            self.hp -=dmg
            print(f"{self.monster.title} {self.monster.name} got hit for {dmg} damage!")
        else:
            print("The Hit doesn't do any damage!")

    @property
    def is_alive(self) -> bool:
        return self.hp <= 0





class Combat:
    def __init__(self, combatant1: Combatant, combatant2: Combatant) -> None:
        self.combatant1 = combatant1
        self.combatant2 = combatant2


    def combat(self) -> None:
        while self.combatant1.is_alive and self.combatant2.is_alive:
            for attack in self.combatant1.get_attacks():
                self.combatant2.defense(attack)
                if not self.combatant2.is_alive:
                    continue

            for attack in self.combatant2.get_attacks():
                self.combatant1.defense(attack)
                if not self.combatant1.is_alive:
                    continue



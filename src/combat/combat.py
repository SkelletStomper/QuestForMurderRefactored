from src.entities.monster import Monster

from src.combat.attack import Attack


def attack_dodged(accuracy: int, dodge: int) -> bool:
    from src.util.dice import d
    dice_dodge = d(8)
    if dice_dodge == 1:
        return False
    if dice_dodge == 8:
        return True

    dice_accuracy = d(6)

    return (accuracy + dice_accuracy) < (dodge + dice_dodge - 1)


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
        le = self.monster.get_le()
        print(f"{le.name} attacks!")

        dmg = self.monster.dmg
        text = "{}"
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
            print(f"{le.name} dodged the attack!")
            return False

        dmg_factor = self.monster.calculate_dmg_factor(attack)
        dmg = round(attack.dmg*dmg_factor)
        dmg -= self.monster.armor

        if dmg > 0:
            dmg = round(dmg*attack.crt)
            self.hp -= dmg
            print(f"{le.name} got hit for {dmg} damage!")
            return True
        else:
            print(f"The hit doesn't penetrate {le.owns} armor!")
            return False

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def status_message(self):
        le = self.monster.get_le()
        print(f"{le.name.capitalize()} has {self.hp} hit points left!")


class MonsterCombat:
    def __init__(self, combatant1: MonsterCombatant, combatant2: MonsterCombatant) -> None:
        self.combatant1 = combatant1
        self.combatant2 = combatant2

    def combat(self) -> None:
        while self.combatant1.is_alive and self.combatant2.is_alive:
            for attack in self.combatant1.get_attacks():
                self.combatant2.defense(attack)
                if not self.combatant2.is_alive:
                    continue
            self.combatant1.status_message()

            for attack in self.combatant2.get_attacks():
                self.combatant1.defense(attack)
                if not self.combatant1.is_alive:
                    continue
            self.combatant1.status_message()

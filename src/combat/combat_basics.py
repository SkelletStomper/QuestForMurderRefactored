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

from items.armor import ArmorMaterial
from src.entities.entity import Entity
from src.items.inventory import Inventory, Item
from src.items.weapon import WeaponAttackStencil
from src.combat.combat_basics import Attack


class NPC(Entity):
    def __init__(self,
                 name: str,
                 title: str = "",
                 pronouns: str = "3rd_they",
                 hp_max: int = 10,
                 dodge: int = 0,
                 accuracy: int = 0,
                 armor: dict[str, int] = None,
                 flags: list[str] | None = None,
                 species: str = "spec_human",
                 inventoryCopy: Inventory|None = None,
                 ) -> None:

        if armor is None:
            armor = {"skin": 0}

        super().__init__(
            name=name,
            title=title,
            pronouns=pronouns,
            hp_max=hp_max,
            dodge=dodge,
            accuracy=accuracy,
            armor=armor,
            flags=flags,
            species=species
        )

        self.hp = self.hp_max
        if inventoryCopy is None:
            self.inventory: Inventory = Inventory(self)
        else:
            self.inventory = inventoryCopy

    def calculate_dmg_factor(self, attack: Attack) -> float:
        """
        Calculate the damage factor of a given attack against this NPC.
        Takes into perspective the weaknesses of all Flags.
        """
        return super().calculate_dmg_factor(attack)

    def get_attack_stencils(self) -> list[WeaponAttackStencil]:
        equip_effects = self.inventory.calculate_bonus()
        return equip_effects.granted_attacks

    def armor_layers(self) -> dict[ArmorMaterial, int]:
        armor = super().armor_layers()
        equip_effects = self.inventory.calculate_bonus()
        for armor_type, armor_value in equip_effects.armor.items():
            if not armor_type in armor.keys():
                armor[armor_type] = 0
            armor[armor_type] += armor_value
        return armor


    def calculate_effective_armor(self, attack: Attack) -> int:

        armor_sum = 0

        for armor_type, armor_value in self.armor_layers().items():
            factor = armor_type.effective_factor(attack.types)
            armor_sum += armor_value*factor

        return round(armor_sum)


    def __repr__(self) -> str:
        return f"NPC(name={self.name}, title={self.title}, pronouns={self.pronouns}, " \
               f" hp_max={self.hp_max}, dodge={self.dodge}, armor={self.armor}, " \
               f"inventory={self.inventory}, flags={self.flags})"

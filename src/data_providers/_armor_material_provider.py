from src.items.armor import ArmorMaterial


class ArmorMaterialProvider:
    def __init__(self, armat_dict: dict[str, dict]):
        self.armats: dict[str, ArmorMaterial] = {}

        for armat_id, armat_data in armat_dict.items():
            self.armats[armat_id] = ArmorMaterial(armat_id, armat_data)

    def __getitem__(self, item: str):
        return self.armats[item]

    def __repr__(self):
        return f"ArmorMaterialProvider({len(self.armats)} Armor Materials)"

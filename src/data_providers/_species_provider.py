from src.entities.species import Species


class SpeciesProvider:
    def __init__(self, species_dict: dict[str, dict]):
        self.species: dict[str, Species] = {}

        for species_id, species_data in species_dict.items():
            self.species[species_id] = Species(species_id, species_data)

        while True:
            changed = False
            for species in self.species.values():
                if not species.full_fledged():
                    parent = self.species[species.subspecies_of]
                    if parent.full_fledged():
                        species.inherit(self)
                        changed = True

            if not changed:
                break
        for species in self.species.values():
            species.prepare_incomplete()



    def __getitem__(self, item: str):
        return self.species[item]

    def __repr__(self):
        return f"SpeciesProvider({len(self.species)} Species)"


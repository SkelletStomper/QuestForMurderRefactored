from src.travel.location import Location




class LocationProvider:
    def __init__(self, location_dict: dict[str, dict]):
        self.locations: dict[str, Location] = {}

        for location_id, location_data in location_dict.items():
            self.locations[location_id] = Location(location_id, location_data)

    def __getitem__(self, item: str):
        return self.locations[item]

    def all_ids(self) -> list[str]:
        return list(self.locations.keys())

    def __repr__(self):
        return f"LocationProvider({len(self.locations)} Locations)"
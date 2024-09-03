from src.effects.effect_base import Effect


class EffectLocationChange(Effect):
    keyword = "location_change"

    def execute(self) -> None:
        from src.state.gamestate import global_state as gs

        location_id = self.parameters[0]

        gs.set_location(location_id)

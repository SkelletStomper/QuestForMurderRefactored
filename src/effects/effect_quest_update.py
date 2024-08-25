from src.effects.effect_base import Effect


class EffectQuestUpdate(Effect):
    keyword = "quest_update"

    def execute(self) -> None:
        from src.state.gamestate import global_state as gs
        quest_log = gs.get_quest_log()
        quest_id = self.parameters[0]
        stage_id = self.parameters[1]

        quest_log.set_quest_stage(quest_id, stage_id)

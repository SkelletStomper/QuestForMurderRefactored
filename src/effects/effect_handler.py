from src.effects.effect_base import Effect
from src.effects.effect_quest_update import EffectQuestUpdate


class EffectHandler:
    registered_effects: dict[str, type[Effect]] = {
        EffectQuestUpdate.keyword: EffectQuestUpdate
    }

    def handle(self, effect_str: str):
        keyword, parameters = self.parse(effect_str)

        to_execute = self.registered_effects[keyword]
        to_execute(parameters).execute()

    @staticmethod
    def parse(effect_str: str) -> tuple[str, list[str]]:
        split = effect_str.split("->")
        keyword = split[0]
        parameters = split[1].split(",")
        return keyword, parameters

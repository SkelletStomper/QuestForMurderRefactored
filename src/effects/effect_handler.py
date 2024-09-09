from src.effects.effect_base import Effect
from src.effects.effect_quest_update import EffectQuestUpdate
from src.effects.effect_location_change import EffectLocationChange
from src.effects.effect_dialogue_start import EffectDialogueStart

class EffectHandler:
    registered_effects: dict[str, type[Effect]] = {
        EffectQuestUpdate.keyword: EffectQuestUpdate,

        EffectLocationChange.keyword: EffectLocationChange,
        EffectDialogueStart.keyword: EffectDialogueStart,
    }

    @staticmethod
    def handle(effect_str: str):
        keyword, parameters = EffectHandler.parse(effect_str)

        to_execute = EffectHandler.registered_effects[keyword]
        to_execute(parameters).execute()

    @staticmethod
    def parse(effect_str: str) -> tuple[str, list[str]]:
        split = effect_str.split("->")
        keyword = split[0]
        parameters = split[1].split(",")
        return keyword, parameters

def apply_effects(effects: list[str]) -> None:
    for effect in effects:
        EffectHandler.handle(effect)

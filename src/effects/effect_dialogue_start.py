from src.effects.effect_base import Effect

class EffectDialogueStart(Effect):
    keyword = "dialogue_start"

    def execute(self) -> None:
        from src.dialogue.dialogue_base import DialogueContext
        dc = DialogueContext()
        dc.start_dialogue(self.parameters[0])


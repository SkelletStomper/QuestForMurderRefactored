from data_providers import quest_provider as qp
from src.quests.quest import Quest, QuestStatus

import logging
logger = logging.getLogger(__name__)


class QuestLog:
    def __init__(self):

        keys = qp.all_ids()

        self.quest_stages = {key: "not_started" for key in keys}

    def set_quest_stage(self, quest_id: str, stage_id: str) -> None:
        if quest_id not in qp.quests:
            logger.warning(f"Tried to set stage to '{stage_id}' for non-existent quest '{quest_id}'")
            raise KeyError("Invalid Quest key when setting quest stage")
        if stage_id not in qp[quest_id].stages:
            logger.warning(f"Tried to set stage for quest '{quest_id}' to non-existent stage '{stage_id}'")
            raise KeyError("Invalid Stage key when setting quest stage")

        self.quest_stages[quest_id] = stage_id

    def quest_counts(self) -> dict[QuestStatus, int]:
        return {
            QuestStatus.IN_PROGRESS: len(qp.get_by_status(QuestStatus.IN_PROGRESS, self.quest_stages)),
            QuestStatus.SUCCESS: len(qp.get_by_status(QuestStatus.SUCCESS, self.quest_stages)),
            QuestStatus.FAILURE: len(qp.get_by_status(QuestStatus.FAILURE, self.quest_stages)),
            QuestStatus.NOT_STARTED: len(qp.get_by_status(QuestStatus.NOT_STARTED, self.quest_stages)),
        }

    def quest_dialogue(self) -> None:

        counts = self.quest_counts()

        currently_viewing = QuestStatus.IN_PROGRESS
        old_viewing = None
        quests = []
        while True:
            if currently_viewing != old_viewing:
                quests = qp.get_by_status(currently_viewing, self.quest_stages)
            old_viewing = currently_viewing

            print(f"In (P)rogress - {counts[QuestStatus.IN_PROGRESS]} "
                  f"| (S)uccess - {counts[QuestStatus.SUCCESS]} "
                  f"| (F)ailure - {counts[QuestStatus.FAILURE]} \n")
            if len(quests) > 0:
                for i, quest in enumerate(quests):
                    print(f"({i+1}): {quest.name}")
            else:
                print("Currently no quests in this Status.")

            print("(0): Back")

            player_input = input(">:").upper()

            if player_input == "P":
                currently_viewing = QuestStatus.IN_PROGRESS
            elif player_input == "S":
                currently_viewing = QuestStatus.SUCCESS
            elif player_input == "F":
                currently_viewing = QuestStatus.FAILURE
            elif player_input == "0":
                return

            elif player_input.isdigit() and 0 <= int(player_input)-1 < len(quests):
                index = int(player_input)-1
                quest: Quest = quests[index]
                print(quest.name)
                print(quest.description)
                stage_id: str = self.quest_stages[quest.id]
                stage: Quest.Stage = quest.stages[stage_id]
                print(f"Current Stage: {stage.name}")
                print(stage.description)
                print(f"Status: {stage.quest_status.value} \n")

            else:
                print("Invalid answer, please try again!")



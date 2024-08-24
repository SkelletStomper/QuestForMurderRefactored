from src.quests.quest import Quest, QuestStatus

import logging
logger = logging.getLogger(__name__)


class QuestProvider:
    def __init__(self, all_quest_data: dict[str, dict]):
        logger.info("Start parsing quest data")
        self.quests: dict[str, Quest] = \
            {quest_name: Quest(quest_name, quest_data)
             for quest_name, quest_data in all_quest_data.items()}
        logger.info("Finished parsing quest data")

    def __getitem__(self, item: str) -> Quest:
        return self.quests[item]

    def all_ids(self) -> list[str]:
        return list(self.quests.keys())

    def get_by_status(self, status: QuestStatus, stage_dict: dict[str, str]) -> list[Quest]:
        return [self.quests[quest_id] for quest_id, stage_id in stage_dict.items()
                if self.quests[quest_id].stages[stage_id].quest_status == status]

    def __repr__(self) -> str:
        return f"QuestProvider({self.quests}) Quest)"

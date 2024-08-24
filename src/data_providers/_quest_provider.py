from src.quests.quest import Quest

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

    def __repr__(self) -> str:
        return f"QuestProvider({self.quests}) Quest)"

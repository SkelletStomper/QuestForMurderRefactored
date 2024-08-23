from enum import Enum


class QuestStatus(Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

class Quest:
    class Stage:
        def __init__(self, stage_id: str, in_dict):
            self.id = stage_id

            self.name = in_dict["name"]
            self.description = in_dict["description"]
            self.quest_status = QuestStatus(in_dict["quest_status"])

            if "following" in in_dict:
                self.following = in_dict["following"]
            else:
                self.following = []




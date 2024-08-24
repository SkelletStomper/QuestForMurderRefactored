from enum import Enum


class QuestStatus(Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class Quest:
    class Stage:
        def __init__(self, stage_id: str, stage_data):
            self.id = stage_id

            self.name = stage_data["name"]
            self.description = stage_data["description"]
            self.quest_status = QuestStatus(stage_data["quest_status"])

            if "following" in stage_data:
                self.following = stage_data["following"]
            else:
                self.following = []

    def __init__(self, quest_id, quest_data):
        self.id = quest_id
        self.name = quest_data["name"]
        self.description = quest_data["description"]
        self.stages: dict[str, Quest.Stage] = \
            {stage_id: self.Stage(stage_id, stage_data)
             for stage_id, stage_data in quest_data["stages"].items()}

        self.stages["not_started"] = self.Stage(
            stage_id="not_started",
            stage_data={
                "name": "Not yet discovered",
                "description": "No Description",
                "quest_status": "NOT_STARTED"
            }
        )




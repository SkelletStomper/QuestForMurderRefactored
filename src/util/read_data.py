import json

import os
from pathlib import Path
from typing import Any


def read_json_data(filename: str) -> dict[str, Any]:
    cwd = os.getcwd()

    highest_dir = cwd.split(os.sep)[-1]
    access_name = ""
    if highest_dir == "src":
        access_name = f"data/{filename}"
    elif highest_dir == "QuestForMurderRefactored":
        access_name = f"src/data/{filename}"
    with open(access_name, "r") as f:
        return json.load(f)



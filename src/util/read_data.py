import json

import os
from typing import Any


def read_json_data(filename: str) -> dict[str, Any]:
    cwd = os.getcwd()

    highest_dir = cwd.split(os.sep)[-1]

    if highest_dir == "src":
        access_name = f"data/{filename}"
    elif highest_dir == "QuestForMurderRefactored":
        access_name = f"src/data/{filename}"
    elif highest_dir == "tests":
        access_name = f"../src/data/{filename}"
    else:
        print(cwd)
        raise RuntimeError("read_json_data does not recognize the cwd")
    with open(access_name, "r") as f:
        return json.load(f)

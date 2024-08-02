import json

import os
from typing import Any


def get_data_folder() -> str:

    cwd = os.getcwd()

    highest_dir = cwd.split(os.sep)[-1]

    if highest_dir == "src":
        access_name = "data"
    elif highest_dir == "QuestForMurderRefactored":
        access_name = "src/data"
    elif highest_dir == "tests":
        access_name = "../src/data"
    else:
        print(cwd)
        raise RuntimeError("read_json_data does not recognize the cwd")
    return access_name


def read_json_data(filename: str) -> dict[str, Any]:
    data_folder = get_data_folder()
    access_name = data_folder + os.sep + filename

    with open(access_name, "r") as f:
        return json.load(f)


def get_all_filenames() -> list[str]:
    data_path = get_data_folder()

    filenames = os.listdir(data_path)
    return filenames

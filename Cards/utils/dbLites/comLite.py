import os
from pathlib import Path

from appdirs import user_data_dir


def local_db():
    appauthor = os.getlogin()
    data_dir = user_data_dir("cards", appauthor, roaming=True)
    os.makedirs(data_dir) if not os.path.exists(data_dir) else ""
    data_dir = Path(data_dir + os.sep + "nba.db")
    return data_dir

def local_banks():
    appauthor = os.getlogin()
    data_dir = user_data_dir("cards", appauthor, roaming=True)
    return Path(data_dir + os.sep + "banks.json")
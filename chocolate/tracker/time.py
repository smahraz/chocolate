from datetime import datetime
from os.path import exists as does_path_exists
from threading import Lock


class LastCheck:
    date = datetime.now()

    _FILE_LOCK = Lock()
    _OUTPUT_PATH = "log/last_check"

    @classmethod
    def update_time(cls) -> None:
        cls.date = datetime.now()
        cls._save_to_file()

    @classmethod
    def get_time(cls) -> datetime:
        return cls.date

    @classmethod
    def _init(cls) -> None:
        if not does_path_exists(cls._OUTPUT_PATH):
            return
        try:
            with open(cls._OUTPUT_PATH, "r") as f:
                date = datetime.fromisoformat(f.read().strip())
            cls.date = date
        except BaseException:
            pass

    @classmethod
    def _save_to_file(cls):
        try:
            with cls._FILE_LOCK:
                with open(cls._OUTPUT_PATH, "w") as f:
                    f.write(str(cls.date))
        except Exception:
            pass


LastCheck._init()

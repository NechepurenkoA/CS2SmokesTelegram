from enum import Enum

MIN_FIELD_LENGTH: int = 5
MAX_FIELD_LENGTH: int = 35
DEFAULT_AUTHOR_VALUE = "Unknown"
URL_TO_UPLOAD_VIDEOS = "videos"
EXTENSION_TO_VALIDATE = "mp4"


class Maps(Enum):
    MIRAGE = "mirage"


class GrenadesType(Enum):
    EXPLOSIVE = "explosive"
    SMOKE = "smoke"
    FLASH = "flash"

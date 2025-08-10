import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Bot configs
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Logs path
DATA_PATH = BASE_DIR / ".data"
BOT_LOGS_FOLDER = DATA_PATH / "bot_logs"

# Logger configs
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")
LOGGING_FORMAT = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
)
LOGS_FILE_PATH = os.path.join(BOT_LOGS_FOLDER, "bot.log")
LOGS_WHEN = os.getenv("LOGS_WHEN", "midnight")
LOGS_INTERVAL = int(os.getenv("LOGS_INTERVAL", 1))
LOGS_BACKUP_COUNT = int(os.getenv("LOGS_BACKUP_COUNT", 14))
LOGS_ENCODING = os.getenv("LOGS_ENCODING", "utf-8")

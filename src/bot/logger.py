import logging
from logging import handlers

from config import (
    BOT_LOGS_FOLDER,
    LOGGING_FORMAT,
    LOGGING_LEVEL,
    LOGS_BACKUP_COUNT,
    LOGS_ENCODING,
    LOGS_FILE_PATH,
    LOGS_INTERVAL,
    LOGS_WHEN,
)


class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = LOGGING_FORMAT

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def configure_logging() -> None:
    BOT_LOGS_FOLDER.mkdir(parents=True, exist_ok=True)
    file_handler = handlers.TimedRotatingFileHandler(
        filename=LOGS_FILE_PATH,
        when=LOGS_WHEN,
        interval=LOGS_INTERVAL,
        backupCount=LOGS_BACKUP_COUNT,
        encoding=LOGS_ENCODING,
    )
    file_handler.setFormatter(CustomFormatter())
    console_handler = logging.StreamHandler()
    logging.basicConfig(
        level=LOGGING_LEVEL,
        format=LOGGING_FORMAT,
        handlers=(file_handler, console_handler),
    )
    logging.getLogger("TELEGRAM_BOT")

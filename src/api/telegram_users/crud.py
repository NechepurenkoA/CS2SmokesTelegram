from api.crud import DatabaseCrud
from telegram_users.models import TelegramUser


class TelegramUserCrud(DatabaseCrud):
    pass


TG_USER_CRUD = TelegramUserCrud(TelegramUser)

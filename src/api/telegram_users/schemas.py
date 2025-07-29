from ninja import Schema


class TelegramUserIn(Schema):
    telegram_id: int


class TelegramUserOut(TelegramUserIn):
    id: int

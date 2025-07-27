from django.db import models


class TelegramUser(models.Model):

    telegram_id = models.BigIntegerField(unique=True)
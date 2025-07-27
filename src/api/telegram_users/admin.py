from django.contrib import admin

from telegram_users.models import TelegramUser


class TelegramUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(TelegramUser, TelegramUserAdmin)

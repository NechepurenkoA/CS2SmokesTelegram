from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from lineups.api import router as lineups_router
from telegram_users.api import router as telegram_user_router

api = NinjaAPI(
    title="CS2SmokesTelegram",
    version="1.0.0",
    description="CS2Smokes API",
)

api.add_router("/users/", telegram_user_router)
api.add_router("/lineups/", lineups_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

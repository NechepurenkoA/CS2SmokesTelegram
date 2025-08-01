from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from lineups.api import router as lineups_router
from telegram_users.api import router as telegram_user_router

api = NinjaAPI(
    title="CS2SmokesTelegram",
    version="1.0.0",
    description="CS2Smokes API",
    docs_url="/docs/",
)

api.add_router("users/", telegram_user_router)
api.add_router("lineups/", lineups_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

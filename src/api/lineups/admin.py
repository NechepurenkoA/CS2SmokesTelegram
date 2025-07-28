from django.contrib import admin

from lineups.models import Lineup


class LineupAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "map",
        "grenade_type",
        "pub_date",
    ]
    list_filter = [
        "map",
        "grenade_type",
        "pub_date",
    ]


admin.site.register(Lineup, LineupAdmin)

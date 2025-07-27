from django.contrib import admin

from lineups.models import Lineup


class LineupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lineup, LineupAdmin)

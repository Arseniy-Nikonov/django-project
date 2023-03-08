from django.contrib import admin

from .models import PlayerStatistics,GameStatistics

admin.site.register(PlayerStatistics)
admin.site.register(GameStatistics)
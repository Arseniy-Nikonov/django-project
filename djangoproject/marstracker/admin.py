from django.contrib import admin

from .models import PlayerStatistics,GameStatistics,Player

admin.site.register(PlayerStatistics)
admin.site.register(GameStatistics)
admin.site.register(Player)
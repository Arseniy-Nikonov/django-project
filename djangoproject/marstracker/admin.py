from django.contrib import admin

from .models import Game,Player,GameResults


admin.site.register(Game)
admin.site.register(Player)
admin.site.register(GameResults)
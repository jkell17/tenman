from django.contrib import admin

from .models import Player, Competition, Game

admin.site.register(Player)
admin.site.register(Competition)
admin.site.register(Game)
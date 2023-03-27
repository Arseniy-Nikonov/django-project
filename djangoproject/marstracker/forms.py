from django import forms
from .models import Player,Game

class GameForm(forms.Form):
    final_score = forms.IntegerField()
    milestones_score = forms.IntegerField()
    awards_score = forms.IntegerField()
    tr_score = forms.IntegerField()
    card_score = forms.IntegerField()
    board_score = forms.IntegerField()

class PlayerForm(GameForm):
    player = forms.ModelMultipleChoiceField(Player.objects.all())

class GamesForm(forms.ModelForm):
    number_of_players = forms.IntegerField(min_value = 1, max_value =8)
    class Meta:
        model = Game
        fields = ['map_type']
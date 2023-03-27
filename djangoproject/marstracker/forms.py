from django import forms
from .models import Player

class PlayerForm(forms.Form):
    # player = forms.ModelMultipleChoiceField(Player.objects.all())
    final_score = forms.IntegerField()
    milestones_score = forms.IntegerField()
    awards_score = forms.IntegerField()
    tr_score = forms.IntegerField()
    card_score = forms.IntegerField()
    board_score = forms.IntegerField()

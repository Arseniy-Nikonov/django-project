from django import forms

class PlayerForm(forms.Form):
    first_name = forms.CharField(label='First name',max_length = 50)
    last_name = forms.CharField(max_length = 50)
    final_score = forms.IntegerField()
    milestones_score = forms.IntegerField()
    awards_score = forms.IntegerField()
    tr_score = forms.IntegerField()
    card_score = forms.IntegerField()
    board_score = forms.IntegerField()

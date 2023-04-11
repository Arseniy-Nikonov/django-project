from django import forms
from .models import Player,Game
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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





# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
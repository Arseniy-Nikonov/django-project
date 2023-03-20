from django.db import models
from datetime import datetime

class Player(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    reg_date = models.DateField('Registration day',default=datetime.now)
    def __str__(self):
        return self.first_name +' '+ self.last_name


class GameResults(models.Model):
    final_score = models.IntegerField(default = 0)
    milestones_score = models.IntegerField(default = 0)
    awards_score = models.IntegerField(default = 0)
    tr_score = models.IntegerField(default = 0)
    card_score = models.IntegerField(default = 0)
    board_score = models.IntegerField(default = 0)
    pub_date = models.DateField('date played',default=datetime.now)
    def __str__(self):
        return str(self.final_score)

class Game(models.Model):
    pub_date = models.DateField('date played',default=datetime.now)
    players = models.ManyToManyField(Player)
    game_results = models.OneToOneField(GameResults,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        output = ''
        for p in self.players.all():
            output = output + p.first_name + " " + p.last_name + " "
        try:
            output +=" Final score:"+ str(self.game_results.final_score)
        except:
            return output
        return output
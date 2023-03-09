from django.db import models
from datetime import datetime

class Player(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    reg_date = models.DateField('Registration day',default=datetime.now)
    def __str__(self):
        return self.first_name +' '+ self.last_name

class GameStatistics(models.Model):
    pub_date = models.DateField('date played',default=datetime.now)
    players = models.ManyToManyField(Player)
    def __str__(self):
        output = ''
        for p in self.players.all():
            output = output + p.first_name + " " + p.last_name + " "
        return output

class PlayerStatistics(models.Model):
    final_score = models.IntegerField(default = 0)
    milestones_score = models.IntegerField(default = 0)
    awards_score = models.IntegerField(default = 0)
    tr_score = models.IntegerField(default = 0)
    card_score = models.IntegerField(default = 0)
    board_score = models.IntegerField(default = 0)
    pub_date = models.DateField('date played')
    def __str__(self):
        return self.player_name



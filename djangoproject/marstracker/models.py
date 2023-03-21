from django.db import models
from datetime import datetime

class GameResults(models.Model):
    final_score = models.IntegerField(default = 0)
    milestones_score = models.IntegerField(default = 0)
    awards_score = models.IntegerField(default = 0)
    tr_score = models.IntegerField(default = 0)
    card_score = models.IntegerField(default = 0)
    board_score = models.IntegerField(default = 0)
    def __str__(self):
        return str(self.final_score)
        
class Player(models.Model):

    
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    reg_date = models.DateField('Registration day',default=datetime.now)
    scores = models.ForeignKey(GameResults,on_delete=models.CASCADE,null=True)

   

    def __str__(self):
        return self.first_name +' '+ self.last_name




class Game(models.Model):
    pub_date = models.DateField('date played',default=datetime.now)
    players = models.ManyToManyField(Player)

    
    def __str__(self):
        return str(self.players)
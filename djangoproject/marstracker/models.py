from django.db import models
from datetime import datetime
from django.urls import reverse


        
class Player(models.Model):

    
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    reg_date = models.DateField('Registration day',default=datetime.now)

    def __str__(self):
        return self.first_name +' '+ self.last_name

    def get_absolute_url(self):
        return reverse('marstracker:index')
    
class Game(models.Model):
    map_choices = [('S','Standard'),('H','Hellas'),('E','Elysium')]
    map_type = models.CharField(max_length = 50,choices=map_choices,default = 'S')
    pub_date = models.DateField('date played',default=datetime.now)
    players = models.ManyToManyField(Player,through='GameResults',related_name="games")

    
    def __str__(self):
        return str(self.map_type)+ "  " + str(self.pub_date) 
    
class GameResults(models.Model):
    final_score = models.IntegerField(default = 0)
    milestones_score = models.IntegerField(default = 0)
    awards_score = models.IntegerField(default = 0)
    tr_score = models.IntegerField(default = 0)
    card_score = models.IntegerField(default = 0)
    board_score = models.IntegerField(default = 0)
    player = models.ForeignKey(Player,on_delete=models.CASCADE,null=True)
    game = models.ForeignKey(Game,on_delete=models.CASCADE,null=True)
    class Meta:
        unique_together = ('player', 'game')
    def __str__(self):
        return str(self.game) + ' ' + str(self.player)
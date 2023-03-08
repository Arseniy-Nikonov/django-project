from django.db import models

class GameStatistics(models.Model):
    pub_date = models.DateField('date played')
    player = models.CharField(max_length = 30) 
    def __str__(self):
        return self.player.player_name

class PlayerStatistics(models.Model):
    player_name = models.ForeignKey(GameStatistics, 
        on_delete = models.CASCADE)
    final_score = models.IntegerField(default = 0)
    milestones_score = models.IntegerField(default = 0)
    awards_score = models.IntegerField(default = 0)
    tr_score = models.IntegerField(default = 0)
    card_score = models.IntegerField(default = 0)
    board_score = models.IntegerField(default = 0)
    pub_date = models.DateField('date played')
    def __str__(self):
        return self.player_name


    
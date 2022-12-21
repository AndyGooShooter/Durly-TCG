from django.db import models
from django.contrib.postgres.fields import ArrayField
import json





class User(models.Model):
    
    # Credentials
    username = models.CharField(max_length = 128)
    hashed_password = models.CharField(max_length = 2048)
    email = models.EmailField()

    # Account Info
    display_name = models.CharField(max_length = 64)
    pfp = models.ImageField()
    
    # Collection
    collection = models.JSONField(default='null')
        # Copies: {int:copies}
        
        # Source: {int:source}      first digit = 0 --> Trade; id of player
        #                           first digit = 1 --> Pack; type of pack
    
        #                           examples:
        #                           1780, from player with the id 178
        #                           21, from pack type 2 (weekly)
    
        # Rank: {int:ranking}
        # Uses: {int:games_played}
        # Wins: {int:games_won}
        
        # Border: {int:border}      0 for none, 
        #                           1 for Crystal,





class Card(models.Model):
    
    token = models.CharField(max_length = 10)
    rarity = models.IntegerField()
    
    text = models.CharField(max_length=4096)
    cover = models.ImageField()
    
    
from django.db import models
from django.contrib.postgres.fields import ArrayField





class User(models.Model):
    
    # Credentials
    username = models.CharField(max_length = 128)
    hashed_password = models.CharField(max_length = 2048)
    email = models.EmailField()

    # Account Info
    display_name = models.CharField(max_length = 64)
    pfp = models.ImageField()
    
    # Collection
    collection = ArrayField(
        ArrayField(
            models.IntegerField(),    
                                    # Copies: {int:copies}
                                    
                                    # Source: {int:source}      first digit = 0 --> Trad; id of player
                                    #                           first digit = 1 --> Pack; type of pack
                                
                                    #                           examples:
                                    #                           1780, from player 178
                                    #                           21, from pack type 2 (weekly)
                                
                                    # Rank: {int:ranking}
                                    # Uses: {int:games_played}
                                    # Wins: {int:games_won}
                                    
                                    # Border: {int:border}      0 for none, 
                                    #                           1 for Crystal,
            size = 5,
        ),
        size = 200
    ) 
    wishlist = ArrayField(
        models.IntegerField(),  # ID   
        size = 5,
    )





class Card(models.Model):
    
    token = models.CharField(max_length = 10)
    rarity = models.IntegerField()
    
    text = models.CharField(max_length=4096)
    cover = models.ImageField()
    
    
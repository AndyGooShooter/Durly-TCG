from django.db import models
from django.contrib.postgres.fields import ArrayField





class User(models.Model):
    
    # Credentials
    username = models.CharField(max_length = 128)
    hased_password = models.CharField(max_length = 2048)
    email = models.EmailField()

    # Account Info
    display_name = models.CharField(max_length = 64)
    pfp = models.ImageField()
    
    # Collection
    collection = ArrayField(
        ArrayField(
            models.Field(),     # Copies: [0 (not owned), 1 (owned)]
                                # Source: ['NaN' (not owned), 'trade_{int:id}', 'pack_{str:type}']
                                # Rank: {int:ranking}
                                # Uses: {int:games_played}
                                # Wins: {int:games_won}
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
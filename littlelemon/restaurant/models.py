from django.db import models

class Booking(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Guess_number = models.IntegerField()
    Comments = models.CharField(max_length=200)

class Menu(models.Model): 
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    menu_item_description = models.TextField(max_length=1000,)
    

    

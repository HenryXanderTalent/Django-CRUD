from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        '''Sets how the table objects appear in online admin center'''
        return self.name + ' ' + self.description
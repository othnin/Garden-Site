from django.db import models
from django.utils import timezone

class Water(models.Model):
    time = models.DateTimeField(auto_now_add=True, unique=True)
    amount = models.IntegerField()

    def __str__(self):
        #return f'{self.time}: {self.amount} gallons'
        return f'{self.time}'

    class Meta:
        verbose_name_plural = 'water'


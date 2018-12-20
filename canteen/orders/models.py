from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Dishes(models.Model):
    dish_name=models.CharField(max_length=200)
    price=models.IntegerField()
    dish_logo=models.CharField(max_length=1000)
    cuisines=models.CharField(max_length=200)
    estimated_time=models.IntegerField()

    def __str__(self):
        return self.dish_name
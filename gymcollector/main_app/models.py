from django.db import models

# Create your models here.
class Exercise(models.Model):
    Type of workout = models.CharField(max_length=100)
    duration = models.IntegerField()
    description = models.TextField(max_length=250)
from django.db import models
from django.urls import reverse
# Create your models here.
class Exercise(models.Model):
    TypeOfWorkout = models.CharField(max_length=100)
    duration = models.IntegerField()
    description = models.TextField(max_length=250)



    def __str__(self):
        return self.TypeOfWorkout


    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    

class Plan(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    description = models.TextField(max_length=250)


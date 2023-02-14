from django.db import models
from django.urls import reverse




# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meals_detail', kwargs={'pk': self.id})

class Exercise(models.Model):
    TypeOfWorkout = models.CharField(max_length=100)
    duration = models.IntegerField()
    description = models.TextField(max_length=250)



    def __str__(self):
        return self.TypeOfWorkout


    def get_absolute_url(self):
        return reverse('exercises_detail', kwargs={'pk': self.id})
    

class Plan(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    goal = models.TextField(max_length=250)
    exercises = models.ManyToManyField(Exercise)
    meals = models.ManyToManyField(Meal)

    

   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plan_id': self.id})




class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    body = models.TextField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE,related_name='Comments')
    created = models.DateTimeField(auto_now_add=True)
    

    def__str__(self):
        return f'comment from {self.name} on {self.exercise}'


    
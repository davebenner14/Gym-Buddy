from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)
    meals = models.ManyToManyField(Meal)

    

   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plan_id': self.id})




class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True, blank=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.meal_id:
            return f"Photo for meal_id: {self.meal_id} @{self.url}"
        elif self.exercise_id:
            return f"Photo for exercise_id: {self.exercise_id} @{self.url}"

    

from django.shortcuts import render
from .models import Exercise

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def exercise_index(request):
  exercise = Exercise.objects.all()
  return render(request, 'exercise/index.html', {
    'exercises': exercises
  })

from django.shortcuts import render
from .models import Exercise

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def exercises_index(request):
  exercises = Exercise.objects.all()
  return render(request, 'exercises/index.html', {
    'exercises': exercises
  })

from django.shortcuts import render
from django.views.generic.edit import CreateView
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


def exercises_detail(request, exercise_id):
  exercise = Exercise.objects.get(id=exercise_id)
  return render(request, 'exercises/detail.html', { 'exercise': exercise})


class ExerciseCreate(CreateView):
  model = Exercise
  fields = '__all__'
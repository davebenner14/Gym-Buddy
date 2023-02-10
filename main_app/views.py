from django.shortcuts import render
from .models import Exercise, Plan

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

def plans_index(request):
  plans = Plan.objects.all()
  return render(request, 'plans/index.html', {
    'plans': plans
  })

def plans_detail(request, plan_id):
  plan = Plan.objects.get(id=plan_id)
  return render(request, 'plans/detail.html', { 'plan': plan })
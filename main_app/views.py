from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Exercise, Plan

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# def exercises_index(request):
#   exercises = Exercise.objects.all()
#   return render(request, 'exercises/index.html', {
#     'exercises': exercises
#   })


# def exercises_detail(request, exercise_id):
#   exercise = Exercise.objects.get(id=exercise_id)
#   return render(request, 'exercises/detail.html', { 'exercise': exercise})


class ExerciseCreate(CreateView):
  model = Exercise
  fields = '__all__'



class ExerciseList(ListView):
  model = Exercise



class ExerciseDetail(DetailView):
  model = Exercise

class ExerciseUpdate(UpdateView):
  model = Exercise
  fields = '__all__'

class ExerciseDelete(DeleteView):
  model = Exercise
  success_url = '/exercises' 


def plans_index(request):
  plans = Plan.objects.all()
  return render(request, 'plans/index.html', {
    'plans': plans
  })

def plans_detail(request, plan_id):
  plan = Plan.objects.get(id=plan_id)
  return render(request, 'plans/detail.html', { 'plan': plan })

class PlanCreate(CreateView):
  model = Plan
  fields = '__all__'
  success_url = '/plans/{plan_id}'

class PlanUpdate(UpdateView):
  model = Plan
  fields = ['name', 'weight', 'goal']

# class PlantDelete(DeleteView):
#   model = Plan
#   success_url = '/plans'

class MealList(ListView):
  model = Meal

class MealCreate(CreateView):
  model = Meal
  fields = '__all__'

class MealDetail(DetailView):
  model = Meal

class MealUpdate(UpdateView):
  model = Meal
  fields = ['name', 'price']

class MealDelete(DeleteView):
  model = Meal
  success_url = '/meals'



import uuid
import boto3
import os

from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Exercise, Plan, Meal, Photo

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
  fields = ['name', 'weight', 'goal']

  # fields = '__all__'
  # success_url = '/plans/{plan_id}'

class PlanUpdate(UpdateView):
  model = Plan
  fields = ['name', 'weight', 'goal']

class PlanDelete(DeleteView):
   model = Plan
   success_url = '/plans'

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

def add_photo_for_meal(request, meal_id):
    add_photo(request, meal_id, 'meal')
    return redirect('meals_detail', pk=meal_id)

def add_photo_for_exercise(request, exercise_id):
    add_photo(request, exercise_id, 'exercise')
    return redirect('exercises_detail', pk=exercise_id)


def add_photo(request, model_id, model_type):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            if model_type == 'meal':
                Photo.objects.create(url=url, meal_id=model_id)
            elif model_type == 'exercise':
                Photo.objects.create(url=url, exercise_id=model_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    


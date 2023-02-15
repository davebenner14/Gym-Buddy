import uuid
import boto3
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Exercise, Plan, Meal, Photo, Comment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg


# from .forms import MealForm, ExerciseForm



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
  plans = Plan.objects.filter(user=request.user)
  return render(request, 'plans/index.html', {
    'plans': plans
  })

def plans_detail(request, plan_id):
  plan = Plan.objects.get(id=plan_id)
  return render(request, 'plans/detail.html', { 'plan': plan })

class PlanCreate(LoginRequiredMixin, CreateView):
  model = Plan
  fields = ['name', 'weight', 'goal']

    # This inherited method is called when a
  # valid plan form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user 
    # Let the CreateView do its job as usual
    return super().form_valid(form)

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

def assoc_meal(request, plan_id, meal_id):
  Plan.objects.get(id=plan_id).meals.add(meal_id)
  return redirect('detail', plan_id=plan_id)

def unassoc_meal(request, plan_id, meal_id):
  Plan.objects.get(id=plan_id).meals.remove(meal_id)
  return redirect('detail', plan_id=plan_id)

def assoc_exercise(request, plan_id, exercise_id):
  Plan.objects.get(id=plan_id).exercises.add(exercise_id)
  return redirect('detail', plan_id=plan_id)

def unassoc_exercise(request, plan_id, exercise_id):
  Plan.objects.get(id=plan_id).exercises.remove(exercise_id)
  return redirect('detail', plan_id=plan_id)



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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def add_comment_for_exercise(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        body = request.POST['body']
        rating = request.POST['rating']
        comment = Comment(name=name, body=body, rating=rating, exercise=exercise)
        comment.save()
        average_rating = Comment.objects.filter(exercise=exercise).aggregate(Avg('rating'))['rating__avg']
        exercise.average_rating = round(average_rating, 2) if average_rating is not None else None
        exercise.save()

    return redirect('exercises_detail', pk=pk)

def exercises_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    average_rating = Comment.objects.filter(exercise=exercise).aggregate(Avg('rating'))['rating__avg']
    context = {'exercise': exercise, 'average_rating': average_rating}
    return render(request, 'exercises/exercises_detail.html', context)

def add_comment_for_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        body = request.POST['body']
        rating = request.POST['rating']
        comment = Comment(name=name, body=body, rating=rating, meal=meal)
        comment.save()
        average_rating = Comment.objects.filter(meal=meal).aggregate(Avg('rating'))['rating__avg']
        meal.average_rating = round(average_rating, 2) if average_rating is not None else None
        meal.save()

    return redirect('meals_detail', pk=pk)


def meals_detail(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    average_rating = Comment.objects.filter(meal=meal).aggregate(Avg('rating'))['rating__avg']
    context = {'meal': meal, 'average_rating': average_rating}
    return render(request, 'meals/meal_detail.html', context)

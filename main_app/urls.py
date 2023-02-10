from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('exercises/', views.exercises_index, name='index'),
  path('exercises/<int:exercise_id>/', views.exercises_detail, name='detail'),
  path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
]


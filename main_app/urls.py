from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('exercises/', views.ExerciseList.as_view(), name='exercises_index'),
  path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
  path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercises_detail'),
  path('exercises/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercises_update'),
  path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercises_delete'),
  path('plans/', views.plans_index, name='index'),
  path('plans/<int:plan_id>/', views.plans_detail, name='detail'),
  path('plans/create/', views.PlanCreate.as_view(), name='plans_create'),
  path('plans/<int:pk>/update/', views.PlanUpdate.as_view(), name='plans_update'),
  path('plans/<int:pk>/delete/', views.PlanDelete.as_view(), name='plans_delete'),
  path('meals/', views.MealList.as_view(), name='meals_index'),
  path('meals/create/', views.MealCreate.as_view(), name='meals_create'),
  path('meals/<int:pk>/', views.MealDetail.as_view(), name='meals_detail'),
  path('meals/<int:pk>/update/', views.MealUpdate.as_view(), name='meals_update'),
  path('meals/<int:pk>/delete/', views.MealDelete.as_view(), name='meals_delete'),
  path('exercises/<int:plan_id>/assoc_exercise/<int:exercise_id>/', views.assoc_exercise, name='assoc_exercise'),
]


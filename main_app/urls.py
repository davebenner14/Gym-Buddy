from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('exercises/', views.exercises_index, name='exercise_index'),
  path('exercises/<int:exercise_id>/', views.exercises_detail, name='detail'),
  path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
  path('plans/', views.plans_index, name='index'),
  path('plans/<int:plan_id>/', views.plans_detail, name='detail'),
  path('plans/create/', views.PlanCreate.as_view(), name='plans_create'),
  path('plans/<int:pk>/update/', views.PlanUpdate.as_view(), name='plans_update'),
  # path('plans/<int:pk>/delete/', views.PlanDelete.as_view(), name='plans_delete'),
  path('meals/', views.MealList.as_view(), name='meals_index'),
  path('meals/<int:pk>/', views.MealDetail.as_view(), name='meals_detail'),
]


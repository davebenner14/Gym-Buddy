from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('gyms/', views.gyms_index, name='index'),

]


from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gyms_index(request):
  return render(request, 'gyms/index.html', {
    'gyms': gyms
  })

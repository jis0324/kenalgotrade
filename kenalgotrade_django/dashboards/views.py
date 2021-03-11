from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
  return render(request, 'home.html')

@login_required
def index(request):
  return HttpResponse("Loged In!")

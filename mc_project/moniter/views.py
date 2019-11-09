from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request , 'moniter/index.html')

@login_required()
def home(request):
	return render(request , 'moniter/home.html')

# @login_required()
# def check_emergency()
	

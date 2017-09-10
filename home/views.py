from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request, 'personal/index.html')

def login(request):
    return render(request, 'personal/login.html')

def register(request):
    #if data is posted (from user submission) perform this
    if request.method =='POST':
        #form reads user input
        form = RegistrationForm(request.POST)
        #if the form contains valid data perform this
        if form.is_valid():
            #save information and redirect to specified location
            form.save()
            return redirect('/home')
    #if request method is 'get' generate empty form
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'personal/register.html', args)

def map(request):
    return render(request, 'personal/map.html')

def profile(request):
    return render(request, 'personal/profile.html')

def admin(request):
    return render(request, 'personal/admin.html')

def home(request):
    return render(request, 'personal/index.html')

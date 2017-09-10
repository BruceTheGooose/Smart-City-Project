from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.forms import RegistrationForm

def home(request):
    return render(request, 'accounts/home.html')

def login(request):
    return render(request, 'accounts/login.html')

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
        return render(request, 'accounts/register.html', args)

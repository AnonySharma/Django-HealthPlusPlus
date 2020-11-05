from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
# from .models import User

# Create your views here.
def home(request):
    # return HttpResponse("Home")
    return render(request, "landing.html")

@login_required(login_url='')
def dashboard(request):
    return render(request, "user/dashboard.html")

@login_required(login_url='')
def profile(request):
    return render(request, "user/profile.html")

def login_page(request):
    return render(request, "login.html")

def login_user(request):
    # logout(request)
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')

    username = password = ""
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
        else:
            messages.info(request, 'Username or password is not correct!')
            messages.info(request, 'Account does not exist!')
            print("Incorrect credentials")
            return render(request, 'login.html',{'incorrect_cred':1})

    print("Not Logged In")
    return render(request, 'login.html')

UserModel = get_user_model()
def register_user(request):
    # logout(request)
    username = password = email = ""
    if request.POST:
        username = request.POST.get('username-reg')
        email = request.POST.get('email-reg')
        password = request.POST.get('password-reg')

        user = authenticate(username=username, password=password)
        if not UserModel.objects.filter(username=username).exists():
            user=UserModel.objects.create_user(username, password=password)
            user.save()
        else:
            messages.info(request, 'Username exists already!')
            print("Registered already")
            return render(request, 'login.html',{'goto_signup':1})

    return render(request, 'login.html')

def logout_user(request):
    print("Logged Out")
    logout(request)
    # return HttpResponseRedirect('')
    return render(request, 'loggedout.html')
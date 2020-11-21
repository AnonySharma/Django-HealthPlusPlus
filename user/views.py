from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *
from .forms import *

UserModel = get_user_model()

# Create your views here.
def home(request):
    # return HttpResponse("Home")
    return render(request, "landing.html")

@receiver(post_save, sender=DjangoUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=DjangoUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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
                # listOfUserMeals=[str(elem) for elem in list(UserMeal.objects.filter(user.username==username))]
                # print(UserMeal.objects.all().filter(user.username==username))
                return HttpResponseRedirect('/dashboard/')
        else:
            messages.info(request, 'Username or password is not correct!')
            messages.info(request, 'Account does not exist!')
            print("Incorrect credentials")
            return render(request, 'login.html',{'incorrect_cred':1})

    print("Not Logged In")
    return render(request, 'login.html')

def register_user(request):
    # logout(request)
    username = password = email = fname = lname = ""
    if request.POST:
        username = request.POST.get('username-reg')
        email = request.POST.get('email-reg')
        password = request.POST.get('password-reg')
        fname = request.POST.get('fname')
        # lname = request.POST.get('lname')
        user = authenticate(username=username, password=password)
        if not UserModel.objects.filter(username=username).exists():
            user=UserModel.objects.create_user(username, password=password, email=email, first_name=fname, last_name=lname)
            # our_user=User.objects.create(username=username, email=email, djangouser=user, name=fname+lname)
            user.save()
        else:
            messages.info(request, 'Username exists already!')
            print("Registered already")
            return render(request, 'login.html', {'goto_signup':1})

    return render(request, 'login.html')

@login_required(login_url='')
def logout_user(request):
    print("Logged Out")
    logout(request)
    # return HttpResponseRedirect('')
    return render(request, 'loggedout.html')

@login_required(login_url='')
def add_food_item(request):
    name = tot_cal = fat = chol = carb = prot = vitam = ""
    if request.POST :
        name = request.POST.get('food-name')
        tot_cal = request.POST.get('food-cal')
        fat = request.POST.get('food-fats')
        chol = request.POST.get('food-chol')
        carb = request.POST.get('food-carbs')
        prot = request.POST.get('food-prot')
        vitam = request.POST.get('food-vit')

        if not FoodItem.objects.filter(name=name).exists():
            FoodItem.objects.create(name=name, total_calories=tot_cal, fat=fat, cholesterol=chol, carbohydrate=carb, protiens=prot, vitamins=vitam)
            messages.info(request, 'Food Item added!')
        else:
            messages.info(request, 'Food with same name already exists!')

    listOfFoodItems=[str(elem) for elem in list(FoodItem.objects.all().values_list('name', flat=True))]
    print(listOfFoodItems)
    # listOfUserMeals=UserMeal.objects.all()
    return redirect('/dashboard/', lfi=listOfFoodItems)

@login_required(login_url='')
def add_user_meal(request, pk):
    # print(request.POST)
    UserMealFormSet = inlineformset_factory(Profile, UserMeal, fields=('fooditem',), extra=1)
    # xy=list(i.name for i in DjangoUser.objects.all().first()._meta.fields)
    # tmp=User.objects.all().filter(id=pk)
    user=Profile.objects.all().get(id=pk)
    formset = UserMealFormSet(queryset=UserMeal.objects.none(), instance=user)
    # user=None
    # print(xy)
    # print(pk,type(tmp),type(user))
    # for i in xy:
    #     if i in ["date", "djangouser", "djangouser_id", "email", "id", "name", "usermeal", "username"]:
    #         print(tmp.values(i),user.values(i))

    if request.method == 'POST':
        form = UserMealForm(request.POST)
        formset = UserMealFormSet(request.POST, instance=user)
        # form.save()
        if formset.is_valid():
            form.save()
            return redirect('/')

    context = {'form':formset}
    return render(request, 'add_usermeal.html', context)
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
from uuid import uuid4

UserModel = get_user_model()

# Create your views here.
def home(request):
    return render(request, "landing.html")

@receiver(post_save, sender=DjangoUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email, username=instance.username)

@receiver(post_save, sender=DjangoUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def about(request):
    return render(request, 'about.html')

@login_required(login_url='')
def dashboard(request):
    user = Profile.objects.get(user_id=request.user.id)
    total=UserMeal.objects.all()
    myUserMeals=total.filter(user=user)
    
    allUserMeals=[]
    for food in myUserMeals:
        allUserMeals.append(food.fooditem.all())

    finalFoodItems=[]
    for usermeal in allUserMeals:
        for food_items in usermeal:
            finalFoodItems.append(food_items)
    
    totalCalories=0
    for foods in finalFoodItems:
        totalCalories+=foods.total_calories
    
    isEmpty = myUserMeals.count()==0
    context = {'Total':totalCalories, 'AllFoodItems': finalFoodItems, 'isEmpty':isEmpty}
    return render(request, "user/dashboard.html",context)

@login_required(login_url='')
def profile(request):
    user = Profile.objects.get(user_id=request.user.id)
    myUserMeals=UserMeal.objects.all().filter(user=user)

    fats=chol=carb=prot=vit=0    
    for food in myUserMeals:
        for item in food.fooditem.all():
            fats+=item.fat
            chol+=item.cholesterol
            carb+=item.carbohydrate
            prot+=item.protiens
            vit+=item.vitamins

    total = (fats+chol+carb+prot+vit)/100
    context = dict()
    if total!=0:
        context['data'] = {'Fats': str(round(fats/total, 2)), 'Cholesterol': str(round(chol/total, 2)), 'Carbohydrates': str(round(carb/total, 2)), 'Proteins': str(round(prot/total, 2)), 'Vitamins': str(round(vit/total, 2))}
    
    context['zero'] = total == 0
    return render(request, "user/profile.html", context)

def login_page(request):
    return render(request, "login.html")

def login_user(request):
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
            return render(request, 'login.html',{'incorrect_cred':True})

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

    return redirect('/dashboard/')

@login_required(login_url='')
def add_user_meal(request, pk):
    UserMealFormSet = inlineformset_factory(Profile, UserMeal, fields=('fooditem',), extra=5)
    user = Profile.objects.get(id=request.user.id)
    formset = UserMealFormSet(queryset=UserMeal.objects.none(), instance=user)

    if request.method == 'POST':
        form = UserMealForm(request.POST)
        formset = UserMealFormSet(request.POST, instance=user)
        if formset.is_valid():
            formset.save()
            return redirect('/dashboard/')

    context = {'form':formset}
    return render(request, 'add_usermeal.html', context)
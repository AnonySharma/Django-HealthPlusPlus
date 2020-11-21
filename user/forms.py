from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class UserMealForm(ModelForm):
    class Meta:
        model = UserMeal
        fields = '__all__'
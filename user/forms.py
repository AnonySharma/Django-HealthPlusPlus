from django.forms import ModelForm
from .models import *

class UserMealForm(ModelForm):
    class Meta:
        model = UserMeal
        fields = '__all__'
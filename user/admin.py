from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(FoodItem)
admin.site.register(UserMeal)
admin.site.register(Profile)
from django.db import models
from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your models here.
class User(models.Model):
    djangouser = models.ForeignKey(UserModel, null=True, on_delete=models.CASCADE)
    username= models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "MyUser:"+self.username

class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    email = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True)

class FoodItem(models.Model):
    name = models.CharField(max_length=200, null=True)
    total_calories = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cholesterol = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    carbohydrate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    protiens = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vitamins = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class UserMeal(models.Model):
    user = models.ForeignKey(Profile, null=True ,on_delete=models.CASCADE)
    # fooditem = models.ManyToManyField(FoodItem, null=True ,on_delete=models.CASCADE)
    fooditem = models.ManyToManyField(FoodItem)
    quantity = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.name
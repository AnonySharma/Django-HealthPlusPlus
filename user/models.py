from django.db import models
from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    email = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.first_name

class FoodItem(models.Model):
    name = models.CharField(max_length=200, null=True)
    total_calories = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    fat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    cholesterol = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    carbohydrate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    protiens = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    vitamins = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)

    def __str__(self):
        return self.name

class UserMeal(models.Model):
    user = models.ForeignKey(Profile, null=True ,on_delete=models.CASCADE)
    fooditem = models.ManyToManyField(FoodItem)
    quantity = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.user.first_name
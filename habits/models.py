from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=75)


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_text = models.CharField(max_length=75)
    steak_count = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    categories = models.ManyToManyField(Category)

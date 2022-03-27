from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self) -> str:
        return f"{self.name}"


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_text = models.CharField(max_length=75)
    streak_count = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"{self.habit_text}"

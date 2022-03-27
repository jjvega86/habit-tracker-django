from rest_framework import serializers
from .models import Habit, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class HabitSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Habit
        fields = ['id', 'habit_text', 'streak_count', 'categories', 'user_id']
        depth = 1

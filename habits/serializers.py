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

    def create(self, validated_data):
        categories_data = validated_data.pop("categories")
        habit = Habit.objects.create(**validated_data)
        for category_data in categories_data:
            category = Category.objects.get(name=category_data['name'])
            if category:
                habit.categories.add(category)
            else:
                new_category = Category.objects.create(
                    name=category_data['name'])
                habit.categories.add(new_category)

        return habit

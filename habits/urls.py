from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits_list),
    path('streak/<int:habit_id>/', views.habit_detail),
    path('category/', views.category_list),
]

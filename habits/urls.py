from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits_list),
    path('streak/<int:habit_id>/', views.habit_detail),
    # path('delete-habit/'),
    # path('add-category/'),
    # path('update-habit-categories/'),
]

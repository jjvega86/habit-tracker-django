from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits_list),
    # path('increase-streak/'),
    # path('reset-streak/'),
    # path('delete-habit/'),
    # path('add-category/'),
    # path('update-habit-categories/'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_habits),
    # path('add-habit/'),
    # path('increase-streak/'),
    # path('reset-streak/'),
    # path('delete-habit/'),
    # path('add-category/'),
    # path('update-habit-categories/'),
]

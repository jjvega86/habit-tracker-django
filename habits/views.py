from os import stat
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

# Models + Serializers
from .models import Habit, Category
from .serializers import HabitSerializer, CategorySerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def habits_list(request):
    if request.method == 'GET':
        habits = Habit.objects.filter(user_id=request.user.id)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = HabitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

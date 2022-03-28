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


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_streak(request, habit_id):
    '''
    Update streak counter for habit
    If there's a 'reset' query param, set streak to 0
    Otherwise, increase by 1
    '''
    try:
        habit = Habit.objects.get(id=habit_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if habit.user_id != request.user.id:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    type_param = request.query_params.get('type')
    print(type_param)

    if type_param == 'reset':
        habit.streak_count = 0
    else:
        habit.streak_count += 1

    habit.save()
    serializer = HabitSerializer(habit)
    return Response(serializer.data, status=status.HTTP_200_OK)

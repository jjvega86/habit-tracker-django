from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

# Models + Serializers
from .models import Habit, Category
from .serializers import HabitSerializer, CategorySerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_habits(request):
    habits = Habit.objects.filter(user_id=request.user.id)
    serializer = HabitSerializer(habits, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

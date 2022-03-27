from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

# Models
from .models import Habit, Category


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_habits(request):
    habits = Habit.objects.filter(user_id=request.user.id)

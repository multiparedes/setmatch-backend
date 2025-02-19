from rest_framework.generics import get_object_or_404

from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def user_list(request):
    users = User.objects.all().order_by('created_at')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
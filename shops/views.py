from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_shops(request):
    name_filter = request.GET.get("name")
    if name_filter:
        queryset = Shop.objects.filter(name__icontains=name_filter)
    else:
        queryset = Shop.objects.all()

    serializer = ShopSerializer(queryset, many=True)
    return Response(serializer.data)
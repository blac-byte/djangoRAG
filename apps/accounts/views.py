from django.contrib.auth import get_user_model
from django.http import HttpResponse

from rest_framework.generics import(
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer


User = get_user_model()

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    # Allow unauthenticated users to access this endpoint
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


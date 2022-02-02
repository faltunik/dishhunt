from django.shortcuts import render
from .models import CustomUser
from .manager import CustomUserManager
from .serializers import CustomUserSerializer
from rest_framework import viewsets
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

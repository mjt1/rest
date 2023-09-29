from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

#Define other API endpoints for creating, uodating, and deleting users
@api_view(['GET'])
def get_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Create a Serializer
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Mets:
        model = User
        fields = '__all__'


#Define URL routes
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users),
    path('users/<int:pk>/', views.get_user),
    path('users/new/', views.create_user),
    path('users/update/<int:pk>/', views.update_user),
    path('users/delete/<int:pk>/', views.delete_user),
]

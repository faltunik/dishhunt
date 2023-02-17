from functools import partial
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions
from .models import Dish
from .serializers import DishSerializer
from rest_framework import serializers, viewsets, status




class DishViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    def printLine(self) :
        for _ in range(10):
            print("--", end="")

    def create(self, request):
        mydata = request.data
        self.printLine()
        print(request)
        print(mydata)
        print(request.user)
        self.printLine()
        serializer = DishSerializer(data=mydata)
        if serializer.is_valid():
            print(request)
            print(request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        #super().partial_update(request, *args, **kwargs)
        serializer = DishSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            print(request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            print(request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    


    
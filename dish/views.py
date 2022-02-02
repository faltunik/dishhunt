from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions
from .models import Dish
from .serializers import DishSerializer


class ListDish(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Dish.objects.get(pk=pk)
        except Dish.DoesNotExist:
            raise Http404

    def get(self, request,  format=None):
        queryset = Dish.objects.all()
        serializer = DishSerializer(queryset, many=True)        
        return Response(serializer.data) # why we cannot return just serializer

    def retrieve(self, request, pk= None, format= None):
        queryset = Dish.objects.all()
        dish = get_object_or_404(queryset, pk=pk)
        serializer = DishSerializer(dish)
        return Response(serializer.data)



@api_view(['GET'])
def about(request):
    queryset = Dish.objects.all()
    serializer = DishSerializer(queryset, many=True)       
    return Response(serializer)
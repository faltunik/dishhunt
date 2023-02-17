from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models  import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('title', 'description', 'recipeurl', 'recipeimage', 'hunter' )
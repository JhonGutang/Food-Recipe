from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import FoodRecipe, Ingredient
from .serializers import FoodRecipeSerializer, IngredientSerializer, FoodRecipeUpdateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.

class FoodRecipeListCreateView(generics.ListCreateAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer

class FoodRecipeUpdateView(generics.UpdateAPIView):  # New view for updating a recipe
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeUpdateSerializer  # Use the update serializer without ingredients

class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientByRecipeView(generics.ListAPIView):  # New view for ingredients by recipe ID
    serializer_class = IngredientSerializer

    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        return Ingredient.objects.filter(food_recipe_id=recipe_id)

class FoodRecipeDeleteView(generics.DestroyAPIView):  # New view for deleting a recipe
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer

    def perform_destroy(self, instance):
        # Delete all related ingredients before deleting the recipe
        instance.ingredients.all().delete()  # Delete related ingredients
        instance.delete()  # Delete the recipe 
from django.urls import path
from .views import FoodRecipeListCreateView, IngredientListCreateView, IngredientByRecipeView, FoodRecipeDeleteView, FoodRecipeUpdateView

urlpatterns = [
    path('recipes/', FoodRecipeListCreateView.as_view(), name='foodrecipe-list-create'),
    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient-list-create'),
    path('recipes/<int:recipe_id>/ingredients/', IngredientByRecipeView.as_view(), name='ingredients-by-recipe'),
    path('recipes/<int:pk>/', FoodRecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipes/<int:pk>/update/', FoodRecipeUpdateView.as_view(), name='recipe-update'),  # New URL for updating a recipe
] 
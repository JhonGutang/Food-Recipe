from django.db import models

class FoodRecipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_path = models.ImageField(upload_to='recipes/images/', null=True, blank=True)

class Ingredient(models.Model):
    food_recipe = models.ForeignKey(FoodRecipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255)
    measurements = models.CharField(max_length=255)

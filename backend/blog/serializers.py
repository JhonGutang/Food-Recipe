import base64
import json
from django.core.files.base import ContentFile
from rest_framework import serializers
from .models import FoodRecipe, Ingredient

class Base64ImageField(serializers.ImageField):
    """ Custom serializer field to handle Base64 image data. """

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(';base64,')  # Extract format and base64 content
            ext = format.split('/')[-1]  # Extract extension
            data = ContentFile(base64.b64decode(imgstr), name=f"temp.{ext}")

        return super().to_internal_value(data)

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'measurements']

class FoodRecipeSerializer(serializers.ModelSerializer):
    image_path = Base64ImageField(required=True)  # Use custom Base64 image field
    ingredients = IngredientSerializer(many=True, write_only=True)

    class Meta:
        model = FoodRecipe
        fields = ['id', 'name', 'description', 'image_path', 'ingredients']

    def to_internal_value(self, data):
        if 'ingredients' in data and isinstance(data['ingredients'], str):
            try:
                data['ingredients'] = json.loads(data['ingredients'])
            except json.JSONDecodeError:
                raise serializers.ValidationError({"ingredients": "Invalid JSON format."})

        return super().to_internal_value(data)

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = FoodRecipe.objects.create(**validated_data)

        for ingredient_data in ingredients_data:
            Ingredient.objects.create(food_recipe=recipe, **ingredient_data)

        return recipe

class FoodRecipeUpdateSerializer(serializers.ModelSerializer):
    image_path = Base64ImageField(required=False)  # Image is optional for updates

    class Meta:
        model = FoodRecipe
        fields = ['id', 'name', 'description', 'image_path']  # No ingredients field for updates

from rest_framework import serializers
from .models import Category, Ingredient, Recipe, RecipeIngredient

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'unit']

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(source='recipeingredient_set', many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'preparation_steps', 'prep_time', 'difficulty', 'category', 'ingredients']
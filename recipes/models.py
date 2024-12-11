from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=50)  # Ejemplo: gramos, mililitros

    def __str__(self):
        return self.name


class Recipe(models.Model):
    DIFFICULTY_LEVELS = [
        ('easy', 'Fácil'),
        ('medium', 'Medio'),
        ('hard', 'Difícil'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    preparation_steps = models.TextField()
    prep_time = models.PositiveIntegerField()  # Tiempo en minutos
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
from django.db import models

from Fitness_Tracker.calorie_tracker.choices import MealChoice


class Food(models.Model):
    name = models.CharField(
        max_length=100,
    )

    serving_size = models.PositiveIntegerField()

    meal_type = models.CharField(
        max_length=20,
        choices=MealChoice.choices,
        default=MealChoice.OTHER,
    )

    calories = models.PositiveIntegerField()

    carbs = models.PositiveIntegerField()
    proteins = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()


from django.core.validators import MinValueValidator, MaxValueValidator
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

    profile = models.ForeignKey(
        to='accounts.Profile',
        on_delete=models.CASCADE,
        related_name='foods',
    )

class Steps(models.Model):
    steps = models.PositiveIntegerField()

    profile = models.ForeignKey(
        to='accounts.Profile',
        on_delete=models.CASCADE,
        related_name='steps_count',
    )


class Water(models.Model):
    water = models.PositiveIntegerField()

    profile = models.ForeignKey(
        to='accounts.Profile',
        on_delete=models.CASCADE,
        related_name='water_count',
    )


class Sleep(models.Model):
    hours = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(23)]
    )
    minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(59)]
    )

    profile = models.ForeignKey(
        to='accounts.Profile',
        on_delete=models.CASCADE,
        related_name='sleep_count',
    )


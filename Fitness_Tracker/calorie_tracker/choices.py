from django.db import models


class MealChoice(models.TextChoices):
    BREAKFAST  = "breakfast", "Breakfast"
    LUNCH = "lunch", 'Lunch'
    DINNER = "dinner", "Dinner"
    SNACKS = "snacks", "Snacks"
    OTHER = "other", "Other"
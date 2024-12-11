from django.contrib import admin
from .models import Food

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'carbs', 'proteins', 'fats', 'meal_type')
    list_filter = ('meal_type', 'calories')
    search_fields = ('name', 'meal_type')
    ordering = ('-calories', 'name')
    list_editable = ('calories', 'carbs', 'proteins', 'fats')

admin.site.register(Food, FoodAdmin)
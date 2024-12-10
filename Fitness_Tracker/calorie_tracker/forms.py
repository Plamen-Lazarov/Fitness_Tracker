from django import forms

from Fitness_Tracker.calorie_tracker.models import Food


class FoodBaseForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class FoodCreateForm(FoodBaseForm):
    class Meta:
        model = Food
        exclude = ['profile']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter the name of the food...',
            }),
            'serving_size': forms.NumberInput(attrs={
                'placeholder': 'Enter the serving size...',
            }),
            'meal_type': forms.Select(attrs={
                'placeholder': 'Enter the meal type...',
            }),
            'calories': forms.NumberInput(attrs={
                'placeholder': 'Enter the calories...',
            }),
            'carbs': forms.NumberInput(attrs={
                'placeholder': 'Enter the carbs...',
            }),
            'proteins': forms.NumberInput(attrs={
                'placeholder': 'Enter the proteins...',
            }),
            'fats': forms.NumberInput(attrs={
                'placeholder': 'Enter the fats...',
            }),
        }


class FoodEditForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ['profile']


class FoodDetailsForm(FoodBaseForm):
    class Meta:
        model = Food
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(FoodDetailsForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True


class FoodDeleteForm(FoodBaseForm):
    class Meta:
        model = Food
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(FoodDeleteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

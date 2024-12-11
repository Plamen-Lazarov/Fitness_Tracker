from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView
from Fitness_Tracker.accounts.forms import CustomUserForm, ProfileEditForm
from Fitness_Tracker.accounts.models import Profile
from Fitness_Tracker.calorie_tracker.models import Food, Water, Steps, Sleep


def home_view(request):
    return render(request, 'common/home.html')


class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class HomeView(TemplateView):
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/home_logged_in.html']
        return ['common/home.html']

@login_required
def dashboard(request):
    user_profile = request.user.profile
    foods = Food.objects.filter(profile=user_profile)
    water = Water.objects.filter(profile=user_profile).first()
    steps = Steps.objects.filter(profile=user_profile).first()
    sleep = Sleep.objects.filter(profile=user_profile).first()
    total_food_calories = sum([food.calories for food in foods])
    remaining_calories = user_profile.calories_goal - total_food_calories
    context = {
        'foods': foods,
        'profile': user_profile,
        'total_food_calories': total_food_calories,
        'remaining_calories': remaining_calories,
        'water': water,
        'steps': steps,
        'sleep': sleep,
    }
    return render(request, 'dashboard.html', context)

def about_us(request):
    return render(request, 'common/about-us.html')


class ProfileEditView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileDetailsView(LoginRequiredMixin,DetailView):
    template_name = 'profile/details-profile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

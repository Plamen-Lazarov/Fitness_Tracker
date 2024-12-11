from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from Fitness_Tracker.calorie_tracker.forms import FoodCreateForm, FoodEditForm, FoodDetailsForm, FoodDeleteForm, \
    WaterEditForm, StepsEditForm, SleepEditForm
from Fitness_Tracker.calorie_tracker.models import Food, Water, Steps, Sleep


class FoodCreateView(LoginRequiredMixin,CreateView):
    model = Food
    form_class = FoodCreateForm
    template_name = 'food/create-food.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class FoodEditView(LoginRequiredMixin, UpdateView):
    model = Food
    form_class = FoodEditForm
    pk_url_kwarg = 'food_id'
    template_name = 'food/edit-food.html'
    success_url = reverse_lazy('dashboard')


class FoodDetailsView(LoginRequiredMixin, DetailView):
    model = Food
    form_class = FoodDetailsForm
    pk_url_kwarg = 'food_id'
    template_name = 'food/details-food.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FoodDetailsForm(instance=self.object)
        return context


class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    form_class = FoodDeleteForm
    pk_url_kwarg = 'food_id'
    template_name = 'food/delete-food.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

class WaterEditView(LoginRequiredMixin, UpdateView):
    model = Water
    form_class = WaterEditForm
    pk_url_kwarg = 'water_id'
    template_name = 'food/edit-food.html'
    success_url = reverse_lazy('dashboard')


class StepsEditView(LoginRequiredMixin, UpdateView):
    model = Steps
    form_class = StepsEditForm
    pk_url_kwarg = 'steps_id'
    template_name = 'steps/edit-steps.html'
    success_url = reverse_lazy('dashboard')


class SleepEditView(LoginRequiredMixin, UpdateView):
    model = Sleep
    form_class = SleepEditForm
    pk_url_kwarg = 'sleep_id'
    template_name = 'sleep/edit-sleep.html'
    success_url = reverse_lazy('dashboard')






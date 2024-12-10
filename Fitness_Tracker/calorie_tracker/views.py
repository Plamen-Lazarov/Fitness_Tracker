from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from Fitness_Tracker.calorie_tracker.forms import FoodCreateForm, FoodEditForm, FoodDetailsForm, FoodDeleteForm
from Fitness_Tracker.calorie_tracker.models import Food


class FoodCreateView(CreateView):
    model = Food
    form_class = FoodCreateForm
    template_name = 'food/create-food.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class FoodEditView(UpdateView):
    model = Food
    form_class = FoodEditForm
    pk_url_kwarg = 'food_id'
    template_name = 'food/edit-food.html'
    success_url = reverse_lazy('dashboard')


class FoodDetailsView(DetailView):
    model = Food
    form_class = FoodDetailsForm
    pk_url_kwarg = 'food_id'
    template_name = 'food/details-food.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FoodDetailsForm(instance=self.object)
        return context


class FoodDeleteView(DeleteView):
    model = Food
    form_class = FoodDeleteForm
    pk_url_kwarg = 'food_id'
    template_name = 'food/delete-food.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

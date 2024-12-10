from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from Fitness_Tracker.accounts.forms import CustomUserForm


def home_view(request):
    return render(request, 'common/home.html')

class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/home_logged_in.html']
        else:
            return ['common/home.html']

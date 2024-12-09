from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from Fitness_Tracker.accounts.views import HomeView, UserRegisterView

urlpatterns = [
    path('', HomeView , name='home'),
    path('register/', UserRegisterView.as_view() , name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
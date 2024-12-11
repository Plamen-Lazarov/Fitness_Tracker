from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path, include
from Fitness_Tracker.accounts.views import home_view, UserRegisterView, HomeView, dashboard, ProfileEditView, \
    ProfileDetailsView, about_us

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('register/', UserRegisterView.as_view() , name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('about-us/', about_us, name='about-us'),
    path('profile/', include([
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('details/', ProfileDetailsView.as_view(), name='profile-details'),
    ]) ),
]
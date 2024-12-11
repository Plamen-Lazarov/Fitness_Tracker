from django.urls import path

from Fitness_Tracker.calorie_tracker.views import FoodCreateView, FoodEditView, FoodDetailsView, FoodDeleteView, \
    WaterEditView, StepsEditView, SleepEditView

from django.conf.urls import handler404

handler404 = 'Fitness_Tracker.calorie_tracker.views.custom_404_view'

urlpatterns = [
    path('create/', FoodCreateView.as_view(), name='create-food'),
    path('<int:food_id>/edit/', FoodEditView.as_view(), name='edit-food'),
    path('<int:food_id>/details/', FoodDetailsView.as_view(), name='details-food'),
    path('<int:food_id>/delete/', FoodDeleteView.as_view(), name='delete-food'),
    path('<int:water_id>/water/', WaterEditView.as_view(), name='edit-water'),
    path('<int:steps_id>/steps/', StepsEditView.as_view(), name='edit-steps'),
    path('<int:sleep_id>/sleep/', SleepEditView.as_view(), name='edit-sleep'),

]

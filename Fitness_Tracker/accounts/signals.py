from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import CreateView

from Fitness_Tracker.accounts.models import Profile
from Fitness_Tracker.calorie_tracker.models import Food, Water, Steps, Sleep

UserModel = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance: UserModel, created: bool, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            first_name='user',
            last_name='user',
            age=0,
            weight=0,
            calories_goal=0,
            bio='no bio',
        )

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_related_objects(sender, instance, created, **kwargs):
    if created:
        profile = instance.profile
        Water.objects.create(profile=profile, water=0)
        Steps.objects.create(profile=profile, steps=0)
        Sleep.objects.create(profile=profile, hours=0, minutes=0)
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from Fitness_Tracker.accounts.forms import CustomUserChangeForm, CustomUserForm
from Fitness_Tracker.accounts.models import Profile
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission

UserModel = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('first_name', 'last_name', 'weight', 'age', 'bio')


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    form = CustomUserChangeForm
    add_form = CustomUserForm

    list_display = ('username', 'email')

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', )})
    )

def create_groups_and_permissions(sender, **kwargs):
    superusers_group, created = Group.objects.get_or_create(name='Superusers')
    if created:
        superusers_group.permissions.set(Permission.objects.all())

    staff_group, created = Group.objects.get_or_create(name='Staff')
    if created:
        limited_permissions = Permission.objects.filter(codename__in=[
            'add_food', 'change_food', 'delete_food', 'view_food'
        ])
        staff_group.permissions.set(limited_permissions)

class AccountsConfig(AppConfig):
    name = 'Fitness_Tracker.accounts'

    def ready(self):
        post_migrate.connect(create_groups_and_permissions, sender=self)
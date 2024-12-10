from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Fitness_Tracker.accounts'

    def ready(self):
        import Fitness_Tracker.accounts.signals

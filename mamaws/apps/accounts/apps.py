from django.apps import AppConfig

class AccountsAppConfig(AppConfig):
    name = 'mamaws.apps.accounts'
    verbose_name = 'Accounts'

    def ready(self):
        from . import signals
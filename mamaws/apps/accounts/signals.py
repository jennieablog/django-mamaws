from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from allauth.account.signals import user_signed_up

from .models import Account
from mamaws.apps.events.models import Purchase

@receiver(post_save, sender=Account)
def news_save_handler(sender, **kwargs):
    if settings.DEBUG:
        print(f"{kwargs['instance']} saved.")


@receiver(post_delete, sender=Account)
def news_delete_handler(sender, **kwargs):
    if settings.DEBUG:
        print(f"{kwargs['instance']} deleted.")

@receiver(user_signed_up)
def after_user_signed_up(sender, request, user, **kwargs):
    user.username = user.email
    user.save()

    purchase = Purchase.objects.create(account=user)
    purchase.save()

    user.active_purchase_id = purchase.id
    user.save()

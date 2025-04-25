from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Deposit

@receiver(post_save, sender=Deposit)
def update_account_balance(sender, instance, created, **kwargs):
    if created and instance.account_id:
        account = instance.account_id
        account.balance += instance.total
        account.save()
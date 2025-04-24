from django.db.models.signals import post_save
from django.dispatch import receiver
from customers.models import Customer
from accounts.models import Account

@receiver(post_save, sender=Customer)
def create_customer_account(sender, instance, created,**kwargs):
    if created:
        Account.objects.create(customer_id=instance)
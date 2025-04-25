from django.db.models.signals import post_save
from django.dispatch import receiver
from customers.models import Customer
from accounts.models import Account
from django.contrib.auth.models import Group

@receiver(post_save, sender=Customer)
def associate_customer_to_group(sender, instance, created, **kwargs):
    if created:
        try:
            Account.objects.create(customer_id=instance)
        except Account.DoesNotExist:
            print(f"Não foi possível criar a conta do usuário")
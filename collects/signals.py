from django.db.models.signals import post_save
from django.dispatch import receiver
from collects.models import Collect, Categorie
from accounts.models import Deposit
from collects.services import calculate_deposit

@receiver(post_save, sender = Collect)
def creat_deposit(sender, instance, created, **kwargs):
    if created:
        try:
            categorie = Categorie.objects.get(id=instance.categorie_id.id)
            total = calculate_deposit(instance.weight, categorie.price, categorie.bonus)
            account = instance.customer_id.accounts.first()

            if account:
                Deposit.objects.create(
                collect_id = instance,
                account_id = account,
                total = total
                )
            else:
                print(f"Aviso: Nenhuma conta encontrada para o cliente {instance.customer_id.id} da coleta {instance.id}.")

        except Categorie.DoesNotExist:
           print(f"Categoria com ID {instance.categorie_id_id} não encontrada para a coleta {instance.id}.")
        except AttributeError as e:
            print(f"Erro ao acessar a conta do cliente para a coleta {instance.id}: {e}")
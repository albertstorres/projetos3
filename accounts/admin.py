from django.contrib import admin
from accounts.models import Account, Deposit


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'balance']
    search_fields = ['customer_id', 'balance']


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['collect_id', 'account_id', 'total', 'created_at']
    search_fields = ['collect_id', 'account_id', 'total', 'created_at']

from django.contrib import admin
from administrators.models import Administrator


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    search_fields = ['id', 'first_name', 'last_name', 'email']
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Primeiro nome')),
                ('last_name', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, verbose_name='E-mail')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customers', to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
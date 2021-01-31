# Generated by Django 3.1.5 on 2021-01-30 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favs', '0002_auto_20210129_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favlist',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='list', to=settings.AUTH_USER_MODEL),
        ),
    ]

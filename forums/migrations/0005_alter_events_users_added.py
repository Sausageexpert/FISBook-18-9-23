# Generated by Django 4.1.5 on 2023-09-03 15:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0004_events_users_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='users_added',
            field=models.ManyToManyField(blank=True, related_name='events_added', to=settings.AUTH_USER_MODEL),
        ),
    ]

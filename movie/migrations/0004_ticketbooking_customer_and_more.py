# Generated by Django 4.1 on 2022-09-13 13:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0003_ticketbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketbooking',
            name='Customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticketbooking',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 19, 41, 10, 749659)),
        ),
    ]

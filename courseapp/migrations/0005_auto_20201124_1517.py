# Generated by Django 3.1.3 on 2020-11-24 10:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0004_auto_20201124_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 24, 10, 17, 1, 48416, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-24 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_auto_20201124_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0010_auto_20201124_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(upload_to='../static/images'),
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0019_auto_20201125_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='accepted', max_length=10),
        ),
    ]
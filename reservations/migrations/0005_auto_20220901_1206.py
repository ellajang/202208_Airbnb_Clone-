# Generated by Django 2.2.5 on 2022-09-01 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20220901_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedday',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookedday',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-28 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankloan',
            name='Time_Period',
        ),
    ]

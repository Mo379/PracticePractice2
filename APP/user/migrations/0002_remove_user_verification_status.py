# Generated by Django 4.0.1 on 2022-11-28 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='verification_status',
        ),
    ]
# Generated by Django 4.0.1 on 2022-04-06 12:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0026_alter_userpaper_pap_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpaper',
            name='pap_creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]
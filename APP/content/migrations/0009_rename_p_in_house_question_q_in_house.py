# Generated by Django 4.0.1 on 2022-11-17 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_remove_point_p_link_point_p_in_house_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='p_in_house',
            new_name='q_in_house',
        ),
    ]
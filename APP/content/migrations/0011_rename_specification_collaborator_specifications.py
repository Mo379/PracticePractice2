# Generated by Django 4.0.1 on 2023-01-17 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_remove_collaborator_specification_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaborator',
            old_name='specification',
            new_name='specifications',
        ),
    ]

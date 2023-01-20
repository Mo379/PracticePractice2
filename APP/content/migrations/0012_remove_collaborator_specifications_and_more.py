# Generated by Django 4.0.1 on 2023-01-18 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_rename_specification_collaborator_specifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborator',
            name='specifications',
        ),
        migrations.AddField(
            model_name='collaborator',
            name='specifications',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='content.specification'),
        ),
    ]

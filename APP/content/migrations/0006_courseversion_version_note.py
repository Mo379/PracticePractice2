# Generated by Django 4.0.1 on 2022-11-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_courseversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseversion',
            name='version_note',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
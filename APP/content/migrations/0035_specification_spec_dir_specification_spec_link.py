# Generated by Django 4.0.1 on 2022-04-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0034_specification_spec_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='specification',
            name='spec_dir',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='specification',
            name='spec_link',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
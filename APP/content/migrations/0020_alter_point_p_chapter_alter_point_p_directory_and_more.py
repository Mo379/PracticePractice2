# Generated by Django 4.0.1 on 2022-04-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_alter_point_p_directory_alter_point_p_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='p_chapter',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='p_directory',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='p_moduel',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='p_subject',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='p_topic',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2023-05-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0039_alter_image_url_alter_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
    ]
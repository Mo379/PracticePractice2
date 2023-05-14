# Generated by Django 4.0.1 on 2023-05-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0037_video_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='p_images',
            field=models.ManyToManyField(to='content.Image'),
        ),
        migrations.AddField(
            model_name='point',
            name='p_videos',
            field=models.ManyToManyField(to='content.Video'),
        ),
        migrations.AddField(
            model_name='question',
            name='q_images',
            field=models.ManyToManyField(to='content.Image'),
        ),
    ]

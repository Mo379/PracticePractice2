# Generated by Django 4.0.1 on 2023-06-01 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0045_video_placement'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='in_question_placement',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
# Generated by Django 4.0.1 on 2023-09-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0063_course_generated_content_course_generated_outline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-11-17 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_rename_p_in_house_question_q_in_house'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
    ]
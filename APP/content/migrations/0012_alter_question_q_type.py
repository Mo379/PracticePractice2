# Generated by Django 4.0.1 on 2022-04-06 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_remove_question_q_origin_question_q_board_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]

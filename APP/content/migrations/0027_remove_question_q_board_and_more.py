# Generated by Django 4.0.1 on 2023-04-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0026_point_erased_question_erased'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='q_board',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_board_moduel',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_exam_month',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_exam_num',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_exam_year',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_in_house',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_is_exam',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_level',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_topic',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_type',
        ),
        migrations.AddField(
            model_name='question',
            name='q_number',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

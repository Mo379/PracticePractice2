# Generated by Django 4.0.1 on 2022-04-06 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_question_q_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='q_origin',
        ),
        migrations.AddField(
            model_name='question',
            name='q_board',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='q_board_moduel',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='q_exam_month',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='q_exam_number',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='q_exam_year',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.CharField(default='', max_length=5, null=True),
        ),
    ]
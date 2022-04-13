# Generated by Django 4.0.1 on 2022-04-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_alter_question_q_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='q_level',
        ),
        migrations.AddField(
            model_name='point',
            name='p_chapter',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='point',
            name='p_content',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='point',
            name='p_directory',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='point',
            name='p_link',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='point',
            name='p_moduel',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='point',
            name='p_topic',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='point',
            name='p_unique_id',
            field=models.CharField(db_index=True, default='', max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='p_subject',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
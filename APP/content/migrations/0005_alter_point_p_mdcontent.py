# Generated by Django 4.0.1 on 2022-12-08 13:59

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_question_q_mdcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='p_MDcontent',
            field=mdeditor.fields.MDTextField(default='', null=True),
        ),
    ]
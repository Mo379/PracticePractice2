# Generated by Django 4.0.1 on 2022-09-14 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_rename_icon_id_user_icon_id_organisation_logo_upload_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='billing_details',
        ),
    ]

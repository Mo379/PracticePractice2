# Generated by Django 4.0.1 on 2022-09-04 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_affiliate_approval_status_affiliate_platform_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Icon_id',
            new_name='icon_id',
        ),
        migrations.AddField(
            model_name='organisation',
            name='logo_upload',
            field=models.FileField(blank=True, upload_to='uploads/organisation_logo'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_upload',
            field=models.FileField(blank=True, upload_to='uploads/profile_picture'),
        ),
    ]

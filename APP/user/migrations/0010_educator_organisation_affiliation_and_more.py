# Generated by Django 4.0.1 on 2022-09-04 12:58

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_rename_subjects_admin_specialised_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='educator',
            name='organisation_affiliation',
            field=models.ManyToManyField(blank=True, related_name='educator_org_affiliation', to='user.Organisation'),
        ),
        migrations.AddField(
            model_name='educator',
            name='taught_subjects',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology')], default=[], max_length=84),
        ),
    ]
# Generated by Django 4.0.1 on 2022-09-04 12:07

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_admin_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='educator_affiliation',
            field=models.ManyToManyField(db_index=True, null=True, related_name='student_edu_affiliation', to='user.Educator'),
        ),
        migrations.AddField(
            model_name='student',
            name='organisation_affiliation',
            field=models.ManyToManyField(db_index=True, null=True, related_name='student_org_affiliation', to='user.Organisation'),
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology')], default=[], max_length=84),
        ),
    ]

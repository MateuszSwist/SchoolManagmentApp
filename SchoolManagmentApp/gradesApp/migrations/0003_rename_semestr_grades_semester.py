# Generated by Django 4.2.3 on 2023-08-05 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gradesApp', '0002_alter_grades_options_semester_grades_semestr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grades',
            old_name='semestr',
            new_name='semester',
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-31 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0019_alter_calendarevents_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='day',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='planoflesson',
            name='class_unit',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.DeleteModel(
            name='PlanOfLesson',
        ),
    ]
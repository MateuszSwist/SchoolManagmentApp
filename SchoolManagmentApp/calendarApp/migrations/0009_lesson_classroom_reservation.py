# Generated by Django 4.2.3 on 2023-08-03 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendarApp', '0008_alter_classroomreservation_classroom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='classroom_reservation',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='calendarApp.classroomreservation'),
            preserve_default=False,
        ),
    ]

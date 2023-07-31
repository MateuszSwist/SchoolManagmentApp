# Generated by Django 4.2.3 on 2023-07-31 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0007_alter_student_parent'),
        ('eventApp', '0018_remove_teacher_lesson_type_teacher_lesson_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevents',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='eventApp.teacher'),
        ),
        migrations.AlterField(
            model_name='calendarevents',
            name='connected_to_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_lesson', to='eventApp.lessonreport'),
        ),
        migrations.AlterField(
            model_name='calendarevents',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='eventApp.subject'),
        ),
        migrations.AlterField(
            model_name='lessonreport',
            name='class_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_class_unit', to='usersApp.classunit'),
        ),
        migrations.AlterField(
            model_name='lessonreport',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_subject', to='eventApp.subject'),
        ),
        migrations.AlterField(
            model_name='lessonreport',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_teacher', to='eventApp.teacher'),
        ),
    ]

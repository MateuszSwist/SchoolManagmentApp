# Generated by Django 4.2.3 on 2023-07-23 08:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField(default=2023, validators=[django.core.validators.MinValueValidator(2023)])),
                ('study_year', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('letter_mark', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='users/avatars/anonymous.png', upload_to='users/avatars/')),
                ('phone_number', models.CharField(blank=True, max_length=9, null=True)),
                ('account_type', models.CharField(choices=[('Teacher', 'Teacher'), ('Parent', 'Parent'), ('Student', 'Student')], default='Student', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klasa', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='students_in_class', to='usersApp.classunit')),
                ('user', models.OneToOneField(limit_choices_to={'account_type': 'Student'}, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='usersApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='usersApp.student')),
                ('user', models.OneToOneField(limit_choices_to={'account_type': 'Parent'}, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='usersApp.profile')),
            ],
        ),
    ]

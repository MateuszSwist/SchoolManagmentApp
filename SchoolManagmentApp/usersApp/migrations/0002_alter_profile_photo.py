# Generated by Django 4.2.3 on 2023-07-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='users/avatars/musk.webp', upload_to='users/avatars/'),
        ),
    ]

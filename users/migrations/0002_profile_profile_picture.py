# Generated by Django 5.0.7 on 2024-08-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default_profile_picture.jpg', upload_to='media/'),
        ),
    ]

# Generated by Django 5.2.3 on 2025-07-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]

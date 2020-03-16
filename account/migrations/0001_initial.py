# Generated by Django 3.0.4 on 2020-03-16 08:07

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number_1', models.CharField(max_length=13, verbose_name='First Phone Number')),
                ('phone_number_2', models.CharField(blank=True, max_length=13, null=True, verbose_name='Second Phone Number')),
                ('profile_picture', models.ImageField(default=account.models.get_default_profile_pic_path, upload_to=account.models.get_profile_pic_path, verbose_name='Profile Picture')),
                ('education_background', models.CharField(choices=[('PostGraduate', 'PostGraduate'), ('UnderGraduate', 'UnderGraduate'), ('HighSchool', 'HighSchool')], max_length=30, verbose_name='Educational Background')),
                ('country', models.CharField(max_length=20, verbose_name='Country')),
                ('github_url', models.URLField(blank=True, max_length=150, null=True, verbose_name='Github homepage URL.')),
                ('personal_url', models.URLField(blank=True, max_length=150, null=True, verbose_name='Personal website URL.')),
                ('facebook_account', models.URLField(blank=True, max_length=255, null=True, verbose_name='Facebook profile page.')),
                ('twitter_account', models.URLField(blank=True, max_length=255, null=True, verbose_name='Twitter profile page.')),
                ('linkedin_account', models.URLField(blank=True, max_length=255, null=True, verbose_name='LinkedIn profile page.')),
                ('short_bio', models.CharField(blank=True, max_length=100, null=True, verbose_name='Short Bio')),
                ('bio', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Bio')),
                ('availability', models.CharField(help_text="wether you're available for collaboration with other         developers on theire either Open Source or Private projects", max_length=50, verbose_name='Availability')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='related_user')),
            ],
        ),
    ]

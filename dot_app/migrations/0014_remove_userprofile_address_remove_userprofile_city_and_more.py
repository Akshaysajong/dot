# Generated by Django 4.1.3 on 2023-02-01 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0013_alter_facility_image_destinstion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='contact_person',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='hotel_type',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
    ]

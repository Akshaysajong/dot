# Generated by Django 4.1.3 on 2023-02-24 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0041_merge_20230223_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_type',
        ),
    ]

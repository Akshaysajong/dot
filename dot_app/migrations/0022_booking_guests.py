# Generated by Django 4.1.3 on 2023-02-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0021_icons_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]

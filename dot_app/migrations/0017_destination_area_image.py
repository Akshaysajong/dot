# Generated by Django 4.1.3 on 2023-02-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0016_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination_area',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]

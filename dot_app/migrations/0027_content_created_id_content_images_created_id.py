# Generated by Django 4.1.3 on 2023-02-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0026_destinationarea_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='created_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='content_images',
            name='created_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

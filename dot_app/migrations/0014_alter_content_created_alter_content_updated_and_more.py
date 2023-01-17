# Generated by Django 4.1.3 on 2023-01-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0013_merge_20230117_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content_images',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content_images',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

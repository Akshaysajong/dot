# Generated by Django 4.1.3 on 2023-02-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0020_icons'),
    ]

    operations = [
        migrations.AddField(
            model_name='icons',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

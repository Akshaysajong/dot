# Generated by Django 4.1.3 on 2023-02-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0021_card_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content_images',
            name='cid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
# Generated by Django 4.1.3 on 2023-01-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0020_alter_destinstions_culture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinstions',
            name='culture',
            field=models.TextField(),
        ),
    ]
# Generated by Django 4.1.3 on 2023-01-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0019_alter_destinstions_culture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinstions',
            name='culture',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=8),
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0011_alter_destinstions_destn_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destn_facility',
            name='destinstions',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='destn_facility',
            name='orgatn',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]

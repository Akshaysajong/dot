# Generated by Django 4.1.3 on 2023-01-31 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0012_best_things_staff_department_customer_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

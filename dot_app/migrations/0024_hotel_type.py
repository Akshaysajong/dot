# Generated by Django 4.1.3 on 2023-01-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0023_delete_hotel_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(blank=True, default=None, max_length=200)),
            ],
        ),
    ]
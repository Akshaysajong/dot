# Generated by Django 4.1.3 on 2023-01-12 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='facility_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, default=None)),
                ('discount', models.FloatField(blank=True, default=None)),
                ('total', models.FloatField(blank=True, default=None)),
                ('status', models.BooleanField(default=False)),
                ('dstn_facility', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dot_app.destinstions')),
            ],
        ),
        migrations.CreateModel(
            name='destn_facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=100)),
                ('description', models.CharField(blank=True, default=None, max_length=200)),
                ('types', models.CharField(blank=True, default=None, max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('destinstions', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dot_app.destinstions')),
            ],
        ),
    ]

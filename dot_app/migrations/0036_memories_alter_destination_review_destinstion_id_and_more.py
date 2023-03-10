# Generated by Django 4.1.3 on 2023-02-21 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0035_alter_booking_guests_facility_review_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='memories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinstions', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('destn_facility', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('experience', models.CharField(blank=True, max_length=200, null=True)),
                ('memories', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('visited_date', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('cust_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dot_app.customer')),
            ],
        ),
        migrations.AlterField(
            model_name='destination_review',
            name='destinstion_id',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='destination_review',
            name='user_id',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='facility_review',
            name='destn_facility_id',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='facility_review',
            name='user_id',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='memories_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('memories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dot_app.memories')),
            ],
        ),
    ]

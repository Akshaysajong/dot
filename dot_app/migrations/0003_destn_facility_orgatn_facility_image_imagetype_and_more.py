# Generated by Django 4.1.3 on 2023-01-24 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0002_booking_type_content_coupon_coupon_type_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destn_facility',
            name='orgatn',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dot_app.organization'),
        ),
        migrations.AddField(
            model_name='facility_image',
            name='imagetype',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='facility_price',
            name='dstn_facility',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dot_app.destinstions'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='organization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dot_app.organization'),
        ),
    ]
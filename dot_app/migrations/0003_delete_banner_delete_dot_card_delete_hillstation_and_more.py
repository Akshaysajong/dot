# Generated by Django 4.1.3 on 2023-01-31 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0002_banner_best_things_dot_card_hillstation_honeymoon_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='banner',
        ),
        migrations.DeleteModel(
            name='dot_card',
        ),
        migrations.DeleteModel(
            name='hillstation',
        ),
        migrations.DeleteModel(
            name='honeymoon',
        ),
        migrations.DeleteModel(
            name='national_parks',
        ),
        migrations.DeleteModel(
            name='stays',
        ),
        migrations.DeleteModel(
            name='treking',
        ),
    ]

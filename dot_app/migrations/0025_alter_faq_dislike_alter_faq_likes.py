# Generated by Django 4.1.3 on 2023-02-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_app', '0024_alter_faq_access_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='dislike',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='likes',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-12 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_auto_20191112_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='is_zillow_listing',
        ),
    ]

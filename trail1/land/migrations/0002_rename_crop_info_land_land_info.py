# Generated by Django 3.2.6 on 2021-12-07 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='land',
            old_name='crop_info',
            new_name='land_info',
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-12 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog01', '0005_auto_20200712_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Category',
            new_name='category',
        ),
    ]

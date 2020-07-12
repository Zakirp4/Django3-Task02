# Generated by Django 3.0.7 on 2020-07-12 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog01', '0004_auto_20200712_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cat',
        ),
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog01.Category'),
        ),
    ]
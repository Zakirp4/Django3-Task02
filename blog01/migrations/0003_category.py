# Generated by Django 3.0.7 on 2020-07-12 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog01', '0002_auto_20200712_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
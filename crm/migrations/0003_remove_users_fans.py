# Generated by Django 2.0.2 on 2018-04-25 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20180425_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='fans',
        ),
    ]

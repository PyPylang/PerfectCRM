# Generated by Django 2.0.2 on 2018-05-05 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20180504_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studyrecord',
            old_name='customer',
            new_name='student',
        ),
    ]
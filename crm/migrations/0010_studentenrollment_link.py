# Generated by Django 2.0.2 on 2018-05-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20180504_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentenrollment',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 2.0.2 on 2018-05-06 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_userprofile_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='username',
        ),
    ]
# Generated by Django 2.0.2 on 2018-05-06 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0021_auto_20180506_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentrecord',
            options={'verbose_name_plural': '支付记录'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('crm_table_list', '可以查看kingadmin每张表里所有的数据'), ('crm_table_list_view', '可以访问kingadmin表里每条数据的修改页'), ('crm_table_list_change', '可以对kingadmin表里的每条数据进行修改'), ('crm_table_obj_add_view', '可以访问kingadmin每张表的数据增加页'), ('crm_table_obj_add', '可以对kingadmin每张表进行数据添加')), 'verbose_name_plural': '用户信息（权限）'},
        ),
    ]

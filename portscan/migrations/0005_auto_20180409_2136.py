# Generated by Django 2.0.4 on 2018-04-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portscan', '0004_auto_20180409_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scanitems',
            name='itemid',
            field=models.CharField(default='f0a40674-84fa-430f-949f-940b65ede944', max_length=50, verbose_name='任务编号'),
        ),
    ]

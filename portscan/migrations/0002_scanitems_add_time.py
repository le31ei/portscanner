# Generated by Django 2.0.4 on 2018-04-09 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portscan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanitems',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
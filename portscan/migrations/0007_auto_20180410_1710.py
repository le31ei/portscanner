# Generated by Django 2.0.4 on 2018-04-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portscan', '0006_auto_20180410_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portresult',
            name='service',
            field=models.CharField(max_length=500, verbose_name='服务'),
        ),
        migrations.AlterField(
            model_name='scanitems',
            name='itemid',
            field=models.CharField(default='a13ca9ab-59f0-4f4c-bbf2-0925bf860735', max_length=50, verbose_name='任务编号'),
        ),
    ]
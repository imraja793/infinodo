# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0003_auto_20180511_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='mobile_no',
            field=models.IntegerField(),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_expense', '0005_auto_20180513_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense_on',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=67)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(max_length=23)),
            ],
        ),
        migrations.AddField(
            model_name='addexpense',
            name='cc_ac_no',
            field=models.BigIntegerField(blank=True, default=1, verbose_name='Cr_ac_no'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addexpense',
            name='expensetype',
            field=models.CharField(default=1, max_length=144, verbose_name='Expense Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addexpense',
            name='invoice_id',
            field=models.CharField(default=1, max_length=23, verbose_name='invoice id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addexpense',
            name='order_placed',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 07:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20171015_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('saleId', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]

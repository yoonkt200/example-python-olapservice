# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_auto_20170531_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='isLocationAgree',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='isPushAgree',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_auto_20170530_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='memberKeyId',
            field=models.CharField(default='', max_length=200),
        ),
    ]

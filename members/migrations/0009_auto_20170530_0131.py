# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_seller_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='address',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='isLocationAgree',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='isPushAgree',
        ),
        migrations.AlterField(
            model_name='buyer',
            name='gender',
            field=models.CharField(default='male', max_length=200),
        ),
        migrations.AlterField(
            model_name='seller',
            name='company',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='seller',
            name='gender',
            field=models.CharField(default='male', max_length=200),
        ),
    ]
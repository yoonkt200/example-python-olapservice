# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_buyer_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='memberDivision',
        ),
    ]
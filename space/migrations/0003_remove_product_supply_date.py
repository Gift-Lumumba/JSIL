# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-29 12:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_auto_20200629_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supply_date',
        ),
    ]

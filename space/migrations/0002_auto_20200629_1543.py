# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-29 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]

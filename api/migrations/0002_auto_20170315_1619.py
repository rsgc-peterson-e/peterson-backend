# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Schdeule',
            new_name='Schedule',
        ),
    ]

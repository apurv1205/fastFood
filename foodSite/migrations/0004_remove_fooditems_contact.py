# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 17:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodSite', '0003_auto_20170225_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditems',
            name='contact',
        ),
    ]

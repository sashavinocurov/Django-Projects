# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-15 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshowapp', '0002_auto_20191015_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='release_date',
            field=models.DateField(),
        ),
    ]
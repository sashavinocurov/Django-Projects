# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-18 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_travel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travel',
            name='traveler',
        ),
        migrations.AddField(
            model_name='travel',
            name='traveler',
            field=models.ManyToManyField(related_name='travels', to='travelapp.User'),
        ),
    ]

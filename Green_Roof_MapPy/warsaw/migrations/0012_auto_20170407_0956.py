# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 09:56
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warsaw', '0011_auto_20170407_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greenroof',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='greenroof',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='greenroof',
            name='poly',
        ),
        migrations.AddField(
            model_name='greenroof',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]

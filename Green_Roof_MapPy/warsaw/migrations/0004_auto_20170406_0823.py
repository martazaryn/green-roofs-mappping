# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 08:23
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warsaw', '0003_populate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenroof',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(max_length=2500, srid=4326),
        ),
    ]

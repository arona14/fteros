# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-14 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gds', '0002_segmentsched'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segmentsched',
            old_name='arrival',
            new_name='arrival_date',
        ),
        migrations.RenameField(
            model_name='segmentsched',
            old_name='departure',
            new_name='departure_date',
        ),
        migrations.RenameField(
            model_name='segmentsched',
            old_name='status_list',
            new_name='status',
        ),
    ]

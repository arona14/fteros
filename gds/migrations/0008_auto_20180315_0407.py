# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 11:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gds', '0007_auto_20180315_0352'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='passenger',
            unique_together=set([('firstname', 'lastname', 'birthdate')]),
        ),
    ]

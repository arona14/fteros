# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20180327_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropnet',
            name='airline',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-12 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='class_svc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reward',
            name='airline',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reward',
            name='pax_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
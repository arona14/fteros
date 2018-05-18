# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-17 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_auto_20180517_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupe',
            name='markup',
            field=models.ManyToManyField(null=True, related_name='markup_group', to='crm.Markup'),
        ),
        migrations.AlterField(
            model_name='groupe',
            name='reward',
            field=models.ManyToManyField(null=True, related_name='reward_group', to='crm.Reward'),
        ),
    ]
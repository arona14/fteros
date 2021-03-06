# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-07 13:40
from __future__ import unicode_literals

import crm.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('queue1', models.CharField(blank=True, max_length=25, null=True)),
                ('queue2', models.CharField(blank=True, max_length=25, null=True)),
                ('queue3', models.CharField(blank=True, max_length=25, null=True)),
                ('queue4', models.CharField(blank=True, max_length=25, null=True)),
                ('queue5', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', crm.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('email_itin', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_sched', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_marketting', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_accounting', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_invoice', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_cell', models.CharField(max_length=25)),
                ('phone_home', models.CharField(blank=True, max_length=25, null=True)),
                ('phone_office', models.CharField(blank=True, max_length=25, null=True)),
                ('fax_1', models.CharField(blank=True, max_length=25, null=True)),
                ('fax_2', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('owrt', models.CharField(choices=[('OW', 'One way'), ('RT', 'Round trip'), ('AN', 'Any')], max_length=2)),
                ('from_base_amt', models.FloatField(blank=True, default=0, null=True)),
                ('from_total_amt', models.FloatField(blank=True, default=0, null=True)),
                ('from_com_amt', models.FloatField(blank=True, default=0, null=True)),
                ('to_base_amt', models.FloatField(blank=True, default=50000, null=True)),
                ('to_total_amt', models.FloatField(blank=True, default=50000, null=True)),
                ('to_com_amt', models.FloatField(blank=True, default=50000, null=True)),
                ('class_svc', models.CharField(blank=True, max_length=10, null=True)),
                ('origin', models.CharField(blank=True, default='ANY', max_length=100, null=True)),
                ('destination', models.CharField(blank=True, default='ANY', max_length=100, null=True)),
                ('x_origin', models.CharField(blank=True, max_length=100, null=True)),
                ('x_destination', models.CharField(blank=True, max_length=100, null=True)),
                ('fare_basis', models.CharField(blank=True, default='ANY', max_length=50, null=True)),
                ('tour_code', models.CharField(blank=True, default='ANY', max_length=50, null=True)),
                ('tkt_designator', models.CharField(blank=True, default='ANY', max_length=50, null=True)),
                ('flight_no', models.CharField(blank=True, default='ANY', max_length=150, null=True)),
                ('inbound_flight', models.CharField(blank=True, default='ANY', max_length=150, null=True)),
                ('outbound_flight', models.CharField(blank=True, default='ANY', max_length=150, null=True)),
                ('issued_from', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('issued_until', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('dep_from', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('dep_until', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('ret_from', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('ret_until', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('issued_from_blackout', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('issued_until_blackout', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('dep_from_blackout', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('dep_until_blackout', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('ret_from_blackout', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('ret_until_blackout', models.DateField(blank=True, default='0001-01-01', null=True)),
                ('arc_no', models.CharField(blank=True, default='ANY', max_length=50, null=True)),
                ('via_points', models.CharField(blank=True, default='ANY', max_length=100, null=True)),
                ('x_via_points', models.CharField(blank=True, max_length=100, null=True)),
                ('seasonality', models.CharField(blank=True, max_length=100, null=True)),
                ('trip_type', models.CharField(blank=True, max_length=25, null=True)),
                ('description', models.CharField(blank=True, max_length=600, null=True)),
                ('statut', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('agency_id', models.CharField(max_length=100)),
                ('interface_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_type', models.CharField(choices=[('A', 'Agency'), ('C', 'Corporate'), ('L', 'Leisure'), ('V', 'Vendor'), ('U', 'User')], max_length=5)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('fax', models.CharField(blank=True, max_length=25, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='crm.Affiliate')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dropnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('pax_type', models.CharField(blank=True, max_length=15, null=True)),
                ('airline', models.CharField(blank=True, max_length=5, null=True)),
                ('dropnet_value', models.CharField(blank=True, default='0', max_length=5, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dropnet_contract', to='crm.Contract')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExceptionAirline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('net_value', models.CharField(blank=True, default='0', max_length=5, null=True)),
                ('pub_value', models.CharField(blank=True, default='0', max_length=5, null=True)),
                ('com_value', models.CharField(blank=True, default='0', max_length=5, null=True)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Markup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('net', models.CharField(blank=True, default='0', max_length=5, null=True)),
                ('pub', models.CharField(blank=True, default='0', max_length=5, null=True)),
                ('com', models.CharField(blank=True, default='0', max_length=5, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='markup_contract', to='crm.Contract')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency_markup', to='crm.Customer')),
                ('x_airlines', models.ManyToManyField(related_name='contracts', through='crm.ExceptionAirline', to='crm.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pcc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('pcc_value', models.CharField(blank=True, max_length=50, null=True)),
                ('gds', models.CharField(blank=True, max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_pcc', to='crm.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('pax_type', models.CharField(blank=True, max_length=15, null=True)),
                ('airline', models.CharField(blank=True, max_length=5, null=True)),
                ('reward_value', models.CharField(blank=True, default='0', max_length=5, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward_contract', to='crm.Contract')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency_reward', to='crm.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('gds', models.CharField(blank=True, max_length=30, null=True)),
                ('value', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('relationship', models.CharField(blank=True, max_length=25, null=True)),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=30, null=True)),
                ('passport_no', models.CharField(blank=True, max_length=30, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('traveler_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exceptionairline',
            name='markup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Markup'),
        ),
        migrations.AddField(
            model_name='communication',
            name='agency',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agency', to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='user',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='crm.Role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]

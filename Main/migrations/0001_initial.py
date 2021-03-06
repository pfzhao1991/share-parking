# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-21 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField()),
                ('role', models.CharField(choices=[('L', 'landlord'), ('C', 'car_owner')], max_length=1)),
            ],
        ),
    ]

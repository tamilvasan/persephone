# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0020_auto_20170401_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='date_started',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
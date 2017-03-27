# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0004_auto_20170327_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_api_key',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='github_repo',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='build',
            name='state',
            field=models.IntegerField(choices=[(0, 'Running'), (1, 'Pending Review'), (2, 'Approved'), (3, 'Rejected')], default=0),
        ),
    ]

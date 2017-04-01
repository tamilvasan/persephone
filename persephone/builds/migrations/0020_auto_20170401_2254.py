# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0019_auto_20170331_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='supersede_same_branch_builds',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='branch_name',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='commit_hash',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='state',
            field=models.IntegerField(choices=[(0, 'Initializing'), (1, 'Running'), (2, 'Finishing'), (3, 'Pending Review'), (4, 'No Diff'), (5, 'Approved'), (6, 'Rejected'), (7, 'Failed'), (8, 'Superseeded')], default=0),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-23 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fds', '0002_auto_20180321_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='rank',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Average', 'Average'), ('Worst', 'Worst')], max_length=200),
        ),
    ]

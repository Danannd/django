# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-04 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animation', '0005_auto_20180201_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

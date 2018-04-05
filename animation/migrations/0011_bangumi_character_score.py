# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-25 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animation', '0010_auto_20180204_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bangumi_character',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ani_id', models.IntegerField(blank=True, default=0)),
                ('character_id', models.IntegerField(blank=True, default=0)),
                ('person_id', models.IntegerField(blank=True, default=0)),
                ('person2_id', models.IntegerField(blank=True, default=0)),
                ('ani_name_jp', models.CharField(blank=True, default='', max_length=100)),
                ('ani_name_cn', models.CharField(blank=True, default='', max_length=100)),
                ('character_name_jp', models.CharField(blank=True, default='', max_length=100)),
                ('character_name_cn', models.CharField(blank=True, default='', max_length=100)),
                ('person_name_jp', models.CharField(blank=True, default='', max_length=100)),
                ('person_name_cn', models.CharField(blank=True, default='', max_length=100)),
                ('person2_name_jp', models.CharField(blank=True, default='', max_length=100)),
                ('person2_name_cn', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('bgm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_jp', models.CharField(blank=True, default='', max_length=100)),
                ('bgm_score', models.FloatField(blank=True, default=0.0)),
                ('bgm_votes', models.IntegerField(blank=True, default=0)),
                ('anidb_id', models.IntegerField(blank=True, default=0)),
                ('anidb_score', models.FloatField(blank=True, default=0.0)),
                ('anidb_votes', models.IntegerField(blank=True, default=0)),
                ('sachi_id', models.IntegerField(blank=True, default=0)),
                ('sachi_score', models.FloatField(blank=True, default=0.0)),
                ('sachi_votes', models.IntegerField(blank=True, default=0)),
                ('ann_id', models.IntegerField(blank=True, default=0)),
                ('ann_score', models.FloatField(blank=True, default=0.0)),
                ('ann_votes', models.IntegerField(blank=True, default=0)),
                ('mal_id', models.IntegerField(blank=True, default=0)),
                ('mal_score', models.FloatField(blank=True, default=0.0)),
                ('mal_votes', models.IntegerField(blank=True, default=0)),
                ('ankr_id', models.IntegerField(blank=True, default=0)),
                ('ankr_score', models.FloatField(blank=True, default=0.0)),
                ('ankr_votes', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]

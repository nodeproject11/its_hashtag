# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-01 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post_info',
            fields=[
                ('message', models.TextField()),
                ('story', models.TextField(blank=True)),
                ('time', models.DateTimeField(blank=True)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('no_of_likes', models.IntegerField(blank=True)),
                ('category', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]

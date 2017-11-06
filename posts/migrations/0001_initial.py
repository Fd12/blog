# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-02 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

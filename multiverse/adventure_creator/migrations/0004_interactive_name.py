# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_creator', '0003_auto_20170225_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactive',
            name='name',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
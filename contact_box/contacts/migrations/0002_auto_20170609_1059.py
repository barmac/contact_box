# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.CharField(max_length=128, null=True),
        ),
    ]

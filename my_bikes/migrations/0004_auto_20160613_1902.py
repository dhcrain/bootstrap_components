# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_bikes', '0003_mybike_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybike',
            name='picture',
            field=models.URLField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title_name',
            new_name='title',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 04:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160810_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='content_1',
        ),
    ]

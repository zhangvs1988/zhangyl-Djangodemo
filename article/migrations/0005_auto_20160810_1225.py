# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 04:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20160810_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content_1',
            new_name='content',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='owner',
            new_name='owne',
        ),
    ]

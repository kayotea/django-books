# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_book_in_print'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(),
        ),
    ]
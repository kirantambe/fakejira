# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='no',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=50, unique=True, verbose_name='Ticket Number'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-11 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentdrip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_drips', to='contacts.Contact'),
        ),
    ]

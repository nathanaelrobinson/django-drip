# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-12 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0002_auto_20161011_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentdrip',
            name='message_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='sentdrip',
            name='opened',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='querysetrule',
            name='lookup_type',
            field=models.CharField(choices=[(b'exact', b'exactly'), (b'iexact', b'exactly (case insensitive)'), (b'contains', b'contains'), (b'icontains', b'contains (case insensitive)'), (b'regex', b'regex'), (b'iregex', b'contains (case insensitive)'), (b'gt', b'greater than'), (b'gte', b'greater than or equal to'), (b'lt', b'less than'), (b'lte', b'less than or equal to'), (b'startswith', b'starts with'), (b'endswith', b'starts with'), (b'istartswith', b'ends with (case insensitive)'), (b'iendswith', b'ends with (case insensitive)'), (b'isnull', b'is null (empty value)')], default=b'exact', max_length=12),
        ),
    ]

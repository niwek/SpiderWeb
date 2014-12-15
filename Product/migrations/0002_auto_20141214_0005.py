# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 14, 5, 4, 59, 212000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 14, 5, 5, 13, 216000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

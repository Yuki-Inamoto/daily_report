# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0005_auto_20150527_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]

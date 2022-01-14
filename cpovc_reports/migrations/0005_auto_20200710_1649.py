# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_reports', '0004_auto_20200707_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rptcaseload',
            name='case',
        ),
        migrations.RemoveField(
            model_name='rptcaseload',
            name='county',
        ),
        migrations.RemoveField(
            model_name='rptcaseload',
            name='org_unit',
        ),
        migrations.RemoveField(
            model_name='rptcaseload',
            name='sub_county',
        ),
        migrations.DeleteModel(
            name='RPTCaseLoad',
        ),
    ]

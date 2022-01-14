# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_reports', '0007_auto_20210109_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rptcaseload',
            name='case',
        ),
        migrations.RemoveField(
            model_name='rptcaseload',
            name='org_unit',
        ),
        migrations.RemoveField(
            model_name='rptipopulation',
            name='case',
        ),
        migrations.RemoveField(
            model_name='rptipopulation',
            name='org_unit',
        ),
        migrations.RemoveField(
            model_name='rptipopulation',
            name='person',
        ),
        migrations.DeleteModel(
            name='CCIPopulation',
        ),
        migrations.DeleteModel(
            name='SIPopulation',
        ),
        migrations.DeleteModel(
            name='SystemUsage',
        ),
        migrations.DeleteModel(
            name='RPTCaseLoad',
        ),
        migrations.DeleteModel(
            name='RPTIPopulation',
        ),
    ]

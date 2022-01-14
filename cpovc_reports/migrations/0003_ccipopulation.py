# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0008_auto_20191026_2152'),
        ('cpovc_reports', '0002_sipopulation_systemusage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCIPopulation',
            fields=[
            ],
            options={
                'verbose_name': 'CCI Population',
                'proxy': True,
                'verbose_name_plural': 'CCI Populations',
            },
            bases=('cpovc_forms.ovcplacement',),
        ),
    ]

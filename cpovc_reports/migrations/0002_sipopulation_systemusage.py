# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_auth', '0002_auto_20160812_1353'),
        ('cpovc_forms', '0007_auto_20191005_1927'),
        ('cpovc_reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SIPopulation',
            fields=[
            ],
            options={
                'verbose_name': 'SI Population',
                'proxy': True,
                'verbose_name_plural': 'SI Populations',
            },
            bases=('cpovc_forms.ovcplacement',),
        ),
        migrations.CreateModel(
            name='SystemUsage',
            fields=[
            ],
            options={
                'verbose_name': 'System Usage',
                'proxy': True,
                'verbose_name_plural': 'System Usages',
            },
            bases=('cpovc_auth.appuser',),
        ),
    ]

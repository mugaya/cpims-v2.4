# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0013_auto_20200918_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='OVCCaseLoadView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpims_id', models.IntegerField()),
                ('case_serial', models.CharField(max_length=50)),
                ('date_case_opened', models.DateField()),
                ('case_category', models.CharField(max_length=255)),
                ('case_sub_category', models.CharField(max_length=255)),
                ('case_date', models.CharField(max_length=15)),
                ('intervention', models.CharField(max_length=255)),
                ('org_unit', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Case Load View',
                'db_table': 'vw_cp_cpims_case_load',
                'managed': False,
                'verbose_name_plural': 'Case Loads View',
            },
        ),
        migrations.AlterModelOptions(
            name='ovccaseevents',
            options={'verbose_name': 'Case Event', 'verbose_name_plural': 'Case Events'},
        ),
    ]

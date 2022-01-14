# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0005_auto_20200112_2042'),
        ('cpovc_forms', '0012_ovccaseinformation'),
        ('cpovc_reports', '0005_auto_20200710_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='RPTCaseLoad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('case_serial', models.CharField(max_length=50)),
                ('case_reporter_id', models.CharField(max_length=4)),
                ('case_reporter', models.CharField(max_length=250)),
                ('case_perpetrator_id', models.CharField(max_length=4, null=True)),
                ('case_perpetrator', models.CharField(max_length=250, null=True)),
                ('case_category_id', models.CharField(max_length=4)),
                ('case_category', models.CharField(max_length=250)),
                ('date_of_event', models.DateField(default=django.utils.timezone.now)),
                ('place_of_event_id', models.CharField(max_length=4)),
                ('place_of_event', models.CharField(max_length=250)),
                ('sex_id', models.CharField(max_length=4)),
                ('sex', models.CharField(max_length=10)),
                ('dob', models.DateField(default=django.utils.timezone.now, null=True)),
                ('county_id', models.IntegerField(default=0)),
                ('county', models.CharField(max_length=250, null=True)),
                ('sub_county_id', models.IntegerField(default=0)),
                ('sub_county', models.CharField(max_length=250, null=True)),
                ('org_unit_name', models.CharField(max_length=250, null=True)),
                ('case_status', models.IntegerField()),
                ('intervention_id', models.CharField(max_length=4, null=True)),
                ('intervention', models.CharField(max_length=250, null=True)),
                ('case_year', models.IntegerField(default=0)),
                ('case_month', models.IntegerField(default=0)),
                ('case_quota', models.IntegerField(default=0)),
                ('case_count', models.IntegerField(default=1)),
                ('age_range', models.CharField(max_length=20, null=True, blank=True)),
                ('knbs_age_range', models.CharField(max_length=20, null=True, blank=True)),
                ('age', models.IntegerField(default=0, null=True)),
                ('case_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('system_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('case', models.ForeignKey(to='cpovc_forms.OVCCaseRecord')),
                ('org_unit', models.ForeignKey(to='cpovc_registry.RegOrgUnit')),
            ],
            options={
                'db_table': 'rpt_case_load',
                'verbose_name': 'Protection Case data',
                'verbose_name_plural': 'Protection Cases data',
            },
        ),
    ]

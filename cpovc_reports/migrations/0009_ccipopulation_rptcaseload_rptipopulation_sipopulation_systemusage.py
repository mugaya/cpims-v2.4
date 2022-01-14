# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0005_auto_20200112_2042'),
        ('cpovc_forms', '0013_auto_20200918_1936'),
        ('cpovc_reports', '0008_auto_20210226_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='RPTCaseLoad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('case_serial', models.CharField(max_length=40)),
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
        migrations.CreateModel(
            name='RPTIPopulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('case_serial', models.CharField(max_length=40)),
                ('admission_number', models.CharField(max_length=40)),
                ('org_unit_name', models.CharField(max_length=250, null=True)),
                ('org_unit_type_id', models.CharField(max_length=4, null=True)),
                ('org_unit_type', models.CharField(max_length=250, null=True)),
                ('sex_id', models.CharField(max_length=4)),
                ('sex', models.CharField(max_length=10)),
                ('dob', models.DateField(default=django.utils.timezone.now, null=True)),
                ('age', models.IntegerField(default=0, null=True)),
                ('age_now', models.IntegerField(default=0, null=True)),
                ('age_range', models.CharField(max_length=20, null=True, blank=True)),
                ('knbs_age_range', models.CharField(max_length=20, null=True, blank=True)),
                ('admission_date', models.DateField(default=django.utils.timezone.now)),
                ('admission_type_id', models.CharField(max_length=4)),
                ('admission_type', models.CharField(max_length=250)),
                ('admission_reason_id', models.CharField(max_length=4)),
                ('admission_reason', models.CharField(max_length=250)),
                ('case_status_id', models.IntegerField(default=1)),
                ('case_status', models.CharField(max_length=20)),
                ('case_category_id', models.CharField(max_length=4)),
                ('case_category', models.CharField(max_length=250)),
                ('sub_category_id', models.CharField(max_length=4)),
                ('sub_category', models.CharField(max_length=250)),
                ('discharge_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('discharge_type_id', models.CharField(max_length=4, null=True)),
                ('discharge_type', models.CharField(max_length=250, null=True)),
                ('county_id', models.IntegerField(default=0)),
                ('county', models.CharField(max_length=250, null=True)),
                ('sub_county_id', models.IntegerField(default=0)),
                ('sub_county', models.CharField(max_length=250, null=True)),
                ('system_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('system_timestamp', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('case', models.ForeignKey(to='cpovc_forms.OVCCaseRecord')),
                ('org_unit', models.ForeignKey(to='cpovc_registry.RegOrgUnit')),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson')),
            ],
            options={
                'db_table': 'rpt_inst_population',
                'verbose_name': 'Population Report',
                'verbose_name_plural': 'Population Reports',
            },
        ),
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
            bases=('cpovc_registry.regpersonstypes',),
        ),
    ]

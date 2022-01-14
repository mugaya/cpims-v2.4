# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0005_auto_20200112_2042'),
        ('cpovc_forms', '0013_auto_20200918_1936'),
        ('cpovc_reports', '0006_rptcaseload'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='rptcaseload',
            name='case_serial',
            field=models.CharField(max_length=40),
        ),
    ]

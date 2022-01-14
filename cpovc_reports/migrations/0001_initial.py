# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0003_auto_20190329_1522'),
        ('cpovc_main', '0003_facilitylist'),
        ('cpovc_forms', '0006_auto_20190329_1522'),
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
                ('person_gender_id', models.CharField(max_length=4)),
                ('person_gender', models.CharField(max_length=10)),
                ('person_dob', models.DateField(default=django.utils.timezone.now, null=True)),
                ('report_county_name', models.CharField(max_length=250, null=True)),
                ('report_subcounty_name', models.CharField(max_length=250, null=True)),
                ('report_orgunit_name', models.CharField(max_length=250, null=True)),
                ('case_status', models.IntegerField()),
                ('case_intervention_id', models.CharField(max_length=4, null=True)),
                ('case_intervention', models.CharField(max_length=250, null=True)),
                ('case_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('system_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('case', models.ForeignKey(to='cpovc_forms.OVCCaseRecord')),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson')),
                ('report_county', models.ForeignKey(related_name='rpt_county', to='cpovc_main.SetupGeography')),
                ('report_orgunit', models.ForeignKey(to='cpovc_registry.RegOrgUnit')),
                ('report_subcounty', models.ForeignKey(related_name='rpt_subcounty', to='cpovc_main.SetupGeography')),
            ],
            options={
                'db_table': 'rpt_case_load',
                'verbose_name': 'Protection Case data',
                'verbose_name_plural': 'Protection Cases data',
            },
        ),
    ]

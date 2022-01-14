# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_ovc', '0002_auto_20171101_0433'),
        ('cpovc_registry', '0002_auto_20171101_0433'),
        ('cpovc_forms', '0003_auto_20161019_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='OVCCareAssessment',
            fields=[
                ('assessment_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('domain', models.CharField(max_length=4)),
                ('service', models.CharField(max_length=4)),
                ('service_status', models.CharField(max_length=4)),
                ('service_grouping_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('is_void', models.BooleanField(default=False)),
                ('sync_id', models.UUIDField(default=uuid.uuid1, editable=False)),
            ],
            options={
                'db_table': 'ovc_care_assessment',
            },
        ),
        migrations.CreateModel(
            name='OVCCareEAV',
            fields=[
                ('eav_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('entity', models.CharField(max_length=5)),
                ('attribute', models.CharField(max_length=5)),
                ('value', models.CharField(max_length=25)),
                ('value_for', models.CharField(max_length=10, null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('sync_id', models.UUIDField(default=uuid.uuid1, editable=False)),
            ],
            options={
                'db_table': 'ovc_care_eav',
            },
        ),
        migrations.CreateModel(
            name='OVCCareEvents',
            fields=[
                ('event', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('event_type_id', models.CharField(max_length=4)),
                ('event_counter', models.IntegerField(default=0)),
                ('event_score', models.IntegerField(default=0, null=True)),
                ('date_of_event', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.IntegerField(default=404, null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('sync_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('house_hold', models.ForeignKey(to='cpovc_ovc.OVCHouseHold', null=True)),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson', null=True)),
            ],
            options={
                'db_table': 'ovc_care_events',
            },
        ),
        migrations.CreateModel(
            name='OVCCareF1B',
            fields=[
                ('form_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('domain', models.CharField(max_length=5)),
                ('entity', models.CharField(max_length=5)),
                ('value', models.SmallIntegerField(default=1)),
                ('is_void', models.BooleanField(default=False)),
                ('event', models.ForeignKey(to='cpovc_forms.OVCCareEvents')),
            ],
            options={
                'db_table': 'ovc_care_f1b',
            },
        ),
        migrations.CreateModel(
            name='OVCCarePriority',
            fields=[
                ('priority_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('domain', models.CharField(max_length=4)),
                ('service', models.CharField(max_length=4)),
                ('service_grouping_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('is_void', models.BooleanField(default=False)),
                ('sync_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('event', models.ForeignKey(to='cpovc_forms.OVCCareEvents')),
            ],
            options={
                'db_table': 'ovc_care_priority',
            },
        ),
        migrations.CreateModel(
            name='OVCCareServices',
            fields=[
                ('service_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('service_provided', models.CharField(max_length=250)),
                ('service_provider', models.CharField(max_length=250, null=True)),
                ('place_of_service', models.CharField(max_length=250, null=True)),
                ('date_of_encounter_event', models.DateField(default=django.utils.timezone.now, null=True)),
                ('service_grouping_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('is_void', models.BooleanField(default=False)),
                ('sync_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('event', models.ForeignKey(to='cpovc_forms.OVCCareEvents')),
            ],
            options={
                'db_table': 'ovc_care_services',
            },
        ),
        migrations.AddField(
            model_name='ovccareeav',
            name='event',
            field=models.ForeignKey(to='cpovc_forms.OVCCareEvents'),
        ),
        migrations.AddField(
            model_name='ovccareassessment',
            name='event',
            field=models.ForeignKey(to='cpovc_forms.OVCCareEvents'),
        ),
    ]

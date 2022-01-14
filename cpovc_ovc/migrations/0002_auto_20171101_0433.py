# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0002_auto_20171101_0433'),
        ('cpovc_main', '0003_facilitylist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cpovc_ovc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OVCCluster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('cluster_name', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ovc_cluster',
                'verbose_name': 'OVC Cluster',
                'verbose_name_plural': 'OVC Clusters',
            },
        ),
        migrations.CreateModel(
            name='OVCClusterCBO',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('cbo', models.ForeignKey(to='cpovc_registry.RegOrgUnit')),
                ('cluster', models.ForeignKey(to='cpovc_ovc.OVCCluster')),
            ],
            options={
                'db_table': 'ovc_cluster_cbo',
                'verbose_name': 'OVC Cluster CBO',
                'verbose_name_plural': 'OVC Cluster CBOs',
            },
        ),
        migrations.CreateModel(
            name='OVCEducation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('school_level', models.CharField(max_length=4)),
                ('school_class', models.CharField(max_length=4)),
                ('admission_type', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson')),
            ],
            options={
                'db_table': 'ovc_care_education',
                'verbose_name': 'OVC Care Education',
                'verbose_name_plural': 'OVC Care Education',
            },
        ),
        migrations.CreateModel(
            name='OVCFacility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facility_code', models.CharField(max_length=10, null=True)),
                ('facility_name', models.CharField(max_length=200)),
                ('is_void', models.BooleanField(default=False)),
                ('sub_county', models.ForeignKey(to='cpovc_main.SetupGeography', null=True)),
            ],
            options={
                'db_table': 'ovc_facility',
                'verbose_name': 'OVC Facility',
                'verbose_name_plural': 'OVC Facilities',
            },
        ),
        migrations.CreateModel(
            name='OVCSchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_level', models.CharField(default=b'1', max_length=5, choices=[(b'SLEC', b'ECD'), (b'SLPR', b'Primary'), (b'SLSE', b'Secondary'), (b'SLUN', b'University'), (b'SLTV', b'Tertiary / Vocational')])),
                ('school_name', models.CharField(max_length=200)),
                ('is_void', models.BooleanField(default=False)),
                ('sub_county', models.ForeignKey(to='cpovc_main.SetupGeography')),
            ],
            options={
                'db_table': 'ovc_school',
                'verbose_name': 'OVC school',
                'verbose_name_plural': 'OVC Schools',
            },
        ),
        migrations.AlterField(
            model_name='ovchealth',
            name='facility',
            field=models.ForeignKey(to='cpovc_ovc.OVCFacility'),
        ),
        migrations.AlterField(
            model_name='ovchousehold',
            name='head_identifier',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='ovceducation',
            name='school',
            field=models.ForeignKey(to='cpovc_ovc.OVCSchool'),
        ),
    ]

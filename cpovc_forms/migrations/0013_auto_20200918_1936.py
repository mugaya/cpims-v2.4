# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0005_auto_20200112_2042'),
        ('cpovc_main', '0006_auto_20200914_2015'),
        ('cpovc_forms', '0012_ovccaseinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='OVCCaseLocation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('case', models.ForeignKey(to='cpovc_forms.OVCCaseRecord')),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson')),
                ('report_location', models.ForeignKey(related_name='sub_location', to='cpovc_main.SetupLocation')),
            ],
            options={
                'db_table': 'ovc_case_location',
                'verbose_name': 'Case Area Location',
                'verbose_name_plural': 'Case Area Locations',
            },
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='case_comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='case_org_unit',
            field=models.ForeignKey(blank=True, to='cpovc_registry.RegOrgUnit', null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='case_params',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='case_record',
            field=models.ForeignKey(blank=True, to='cpovc_forms.OVCCaseRecord', null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ovcbasiccrs',
            name='case_id',
            field=models.UUIDField(default=uuid.uuid1, serialize=False, primary_key=True),
        ),
    ]

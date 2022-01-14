# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0017_auto_20211106_1428'),
        ('cpovc_registry', '0006_regpersonsothergeo'),
        ('cpovc_afc', '0003_afcmain_case_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AFCEvents',
            fields=[
                ('event_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('event_count', models.IntegerField(default=1)),
                ('event_date', models.DateField()),
                ('form_id', models.CharField(max_length=3, blank=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('care', models.ForeignKey(to='cpovc_afc.AFCMain')),
                ('case', models.ForeignKey(to='cpovc_forms.OVCCaseRecord')),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson')),
            ],
            options={
                'db_table': 'ovc_afc_event',
                'verbose_name': 'AFC Event',
                'verbose_name_plural': 'AFC Events',
            },
        ),
        migrations.CreateModel(
            name='AFCForms',
            fields=[
                ('form_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('question_id', models.CharField(max_length=12)),
                ('item_value', models.CharField(max_length=5)),
                ('item_detail', models.TextField(null=True, blank=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('event', models.ForeignKey(to='cpovc_afc.AFCEvents')),
            ],
            options={
                'db_table': 'ovc_afc_form',
                'verbose_name': 'AFC Form data',
                'verbose_name_plural': 'AFC Forms data',
            },
        ),
    ]

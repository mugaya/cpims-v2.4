# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0017_auto_20211106_1428'),
        ('cpovc_registry', '0006_regpersonsothergeo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AFCMain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('care_type', models.CharField(max_length=5, blank=True)),
                ('case_date', models.DateField()),
                ('case_status', models.NullBooleanField(default=None)),
                ('case_stage', models.IntegerField(default=0)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestamp_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('case', models.ForeignKey(to='cpovc_forms.OVCCaseRecord')),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson')),
            ],
            options={
                'db_table': 'ovc_afc_main',
                'verbose_name': 'Alternative Care',
                'verbose_name_plural': 'Alternative Cares',
            },
        ),
    ]

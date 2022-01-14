# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0005_auto_20200112_2042'),
        ('cpovc_forms', '0011_auto_20200112_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='OvcCaseInformation',
            fields=[
                ('info_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('info_type', models.CharField(default=b'INFO', max_length=5)),
                ('info_item', models.CharField(max_length=6, null=True)),
                ('info_detail', models.TextField(null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('case', models.ForeignKey(to='cpovc_forms.OVCCaseRecord', null=True)),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson', null=True)),
            ],
            options={
                'db_table': 'ovc_case_info',
                'verbose_name': 'Case Information',
                'verbose_name_plural': 'Case Information',
            },
        ),
    ]

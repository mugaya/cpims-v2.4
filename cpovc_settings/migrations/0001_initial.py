# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0003_auto_20190329_1522'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cpovc_forms', '0006_auto_20190329_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseDuplicates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duplicate_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('case_category_id', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(null=True)),
                ('action_id', models.IntegerField(default=1)),
                ('interventions', models.IntegerField(default=0)),
                ('is_void', models.BooleanField(default=False)),
                ('case', models.ForeignKey(to='cpovc_forms.OVCCaseRecord')),
                ('created_by', models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL, null=True)),
                ('organization_unit', models.ForeignKey(to='cpovc_registry.RegOrgUnit')),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson')),
                ('updated_by', models.ForeignKey(related_name='updator', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'case_duplicates',
                'verbose_name': 'Duplicated case',
                'verbose_name_plural': 'Duplicated Cases',
            },
        ),
    ]

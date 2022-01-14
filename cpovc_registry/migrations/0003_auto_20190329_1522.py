# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0002_auto_20171101_0433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regpersonsgeo',
            options={'verbose_name': 'Person Geographical area (Ward, Sub-county)', 'verbose_name_plural': 'Person Geographical areas (Ward, Sub-county)'},
        ),
        migrations.AlterModelOptions(
            name='regpersonsorgunits',
            options={'verbose_name': 'Persons Organisation Unit', 'verbose_name_plural': 'Persons Organisation Units'},
        ),
        migrations.AlterModelOptions(
            name='regpersonstypes',
            options={'verbose_name': 'Person Type (Child, Caregiver, other)', 'verbose_name_plural': 'Person Types (Child, Caregiver, other)'},
        ),
        migrations.AlterField(
            model_name='regperson',
            name='other_names',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='regpersonsorgunits',
            name='date_delinked',
            field=models.DateField(null=True, blank=True),
        ),
    ]

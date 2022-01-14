# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0010_auto_20191127_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovccasepersons',
            name='person_identifier',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ovccasepersons',
            name='person',
            field=models.ForeignKey(to='cpovc_registry.RegPerson', null=True),
        ),
        migrations.AlterField(
            model_name='ovcdischargefollowup',
            name='actual_return_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ovcdischargefollowup',
            name='discharge_destination',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ovcdischargefollowup',
            name='expected_return_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]

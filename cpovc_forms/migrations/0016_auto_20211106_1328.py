# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0015_auto_20211105_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovccasegeo',
            name='occurence_county',
            field=models.ForeignKey(related_name='occurence_county_fk', to='cpovc_main.SetupGeography', null=True),
        ),
        migrations.AlterField(
            model_name='ovccasegeo',
            name='occurence_subcounty',
            field=models.ForeignKey(related_name='occurence_subcounty_fk', to='cpovc_main.SetupGeography', null=True),
        ),
    ]

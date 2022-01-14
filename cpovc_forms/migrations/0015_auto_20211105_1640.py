# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0014_auto_20211105_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovccaselocation',
            name='report_city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='ovccaselocation',
            name='report_country_code',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='ovccaselocation',
            name='case',
            field=models.OneToOneField(to='cpovc_forms.OVCCaseRecord'),
        ),
        migrations.AlterField(
            model_name='ovccaselocation',
            name='report_location',
            field=models.ForeignKey(related_name='sub_location', to='cpovc_main.SetupLocation', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0007_auto_20210226_1002'),
        ('cpovc_forms', '0016_auto_20211106_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovccaselocation',
            name='report_sublocation',
            field=models.ForeignKey(related_name='sub_location', to='cpovc_main.SetupLocation', null=True),
        ),
        migrations.AlterField(
            model_name='ovccaselocation',
            name='report_location',
            field=models.ForeignKey(related_name='location', to='cpovc_main.SetupLocation', null=True),
        ),
    ]

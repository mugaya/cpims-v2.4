# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0008_auto_20191026_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovccaserecord',
            name='case_remarks',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ovccaserecord',
            name='case_reporter_first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ovccaserecord',
            name='case_reporter_other_names',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ovccaserecord',
            name='case_reporter_surname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ovccaserecord',
            name='perpetrator_first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ovccaserecord',
            name='perpetrator_other_names',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ovccaserecord',
            name='perpetrator_surname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

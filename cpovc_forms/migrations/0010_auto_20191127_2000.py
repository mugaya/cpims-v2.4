# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0009_auto_20191031_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovcplacement',
            name='current_residential_status',
            field=models.CharField(max_length=4, blank=True),
        ),
        migrations.AlterField(
            model_name='ovcplacement',
            name='free_for_adoption',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ovcplacement',
            name='holding_period',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ovcplacement',
            name='ob_number',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ovcplacement',
            name='placement_notes',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ovcplacement',
            name='placement_type',
            field=models.CharField(default=b'Normal', max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='ovcplacement',
            name='transfer_from',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]

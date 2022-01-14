# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0005_listanswers_answer_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setuplocation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='setuplocation',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='setuplocation',
            name='is_void',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='setuplocation',
            name='parent_area_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='setuplocation',
            name='area_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]

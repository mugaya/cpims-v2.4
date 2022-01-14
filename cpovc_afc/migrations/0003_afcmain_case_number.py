# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_afc', '0002_auto_20220107_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='afcmain',
            name='case_number',
            field=models.CharField(max_length=12, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_ctip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctipevents',
            name='case_count',
            field=models.IntegerField(default=1),
        ),
    ]

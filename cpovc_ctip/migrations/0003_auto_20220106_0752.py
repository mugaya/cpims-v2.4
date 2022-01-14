# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_ctip', '0002_ctipevents_case_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ctipevents',
            old_name='case_count',
            new_name='event_count',
        ),
    ]

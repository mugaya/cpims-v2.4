# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0006_auto_20200914_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listanswers',
            old_name='timestamp_modified',
            new_name='timestamp_updated',
        ),
        migrations.RenameField(
            model_name='setuplist',
            old_name='timestamp_modified',
            new_name='timestamp_updated',
        ),
    ]

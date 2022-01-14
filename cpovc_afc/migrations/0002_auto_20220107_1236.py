# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_afc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afcmain',
            name='id',
        ),
        migrations.AddField(
            model_name='afcmain',
            name='care_id',
            field=models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True),
        ),
    ]

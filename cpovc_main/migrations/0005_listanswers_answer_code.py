# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0004_setuplocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='listanswers',
            name='answer_code',
            field=models.CharField(db_index=True, max_length=6, null=True, blank=True),
        ),
    ]

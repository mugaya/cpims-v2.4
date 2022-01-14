# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0004_auto_20191031_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regperson',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
    ]

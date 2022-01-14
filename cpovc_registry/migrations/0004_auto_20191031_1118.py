# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0003_auto_20190329_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovchousehold',
            name='members',
            field=models.TextField(),
        ),
    ]

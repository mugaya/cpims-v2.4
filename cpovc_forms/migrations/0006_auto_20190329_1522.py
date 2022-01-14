# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0005_listbanks_ovcgokbursary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ovccasecategory',
            options={'verbose_name': 'Case Category', 'verbose_name_plural': 'Case Categories'},
        ),
        migrations.AlterModelOptions(
            name='ovccasegeo',
            options={'verbose_name': 'Case Geography', 'verbose_name_plural': 'Case Geographies'},
        ),
        migrations.AlterModelOptions(
            name='ovccaserecord',
            options={'verbose_name': 'Case Record', 'verbose_name_plural': 'Case Records'},
        ),
    ]

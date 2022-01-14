# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0003_facilitylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetupLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_id', models.IntegerField(unique=True)),
                ('area_name', models.CharField(max_length=100)),
                ('area_type_id', models.CharField(max_length=50)),
                ('area_code', models.CharField(max_length=10, null=True)),
                ('parent_id', models.IntegerField()),
            ],
            options={
                'db_table': 'list_location',
            },
        ),
    ]

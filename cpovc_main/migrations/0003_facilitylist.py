# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0002_auto_20160812_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facility_code', models.IntegerField()),
                ('facility_name', models.CharField(max_length=255)),
                ('county_id', models.IntegerField()),
                ('county_name', models.CharField(max_length=255)),
                ('subcounty_id', models.IntegerField()),
                ('subcounty_name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=5)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=5)),
                ('is_void', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'facility_list',
            },
        ),
    ]

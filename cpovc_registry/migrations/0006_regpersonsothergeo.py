# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0007_auto_20210226_1002'),
        ('cpovc_registry', '0005_auto_20200112_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegPersonsOtherGeo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_code', models.CharField(max_length=4, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('date_linked', models.DateField(null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('location', models.ForeignKey(to='cpovc_main.SetupLocation', null=True)),
                ('person', models.OneToOneField(to='cpovc_registry.RegPerson')),
            ],
            options={
                'db_table': 'reg_person_other_geo',
                'verbose_name': 'Person Geo area (Country, City, Location)',
                'verbose_name_plural': 'Person Geo areas (Country, City, Location)',
            },
        ),
    ]

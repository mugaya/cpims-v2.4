# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_reports', '0003_ccipopulation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='report_county',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='case_intervention',
            new_name='county_name',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='person_dob',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='report_county_name',
            new_name='intervention',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='case_intervention_id',
            new_name='intervention_id',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='report_orgunit',
            new_name='org_unit',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='report_orgunit_name',
            new_name='org_unit_name',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='person_gender',
            new_name='sex',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='person_gender_id',
            new_name='sex_id',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='report_subcounty',
            new_name='sub_county',
        ),
        migrations.RenameField(
            model_name='rptcaseload',
            old_name='report_subcounty_name',
            new_name='sub_county_name',
        ),
        migrations.RemoveField(
            model_name='rptcaseload',
            name='person',
        ),
        migrations.AddField(
            model_name='rptcaseload',
            name='age',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='rptcaseload',
            name='age_range',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rptcaseload',
            name='case_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='rptcaseload',
            name='case_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rptcaseload',
            name='case_quota',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rptcaseload',
            name='case_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rptcaseload',
            name='knbs_age_range',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]

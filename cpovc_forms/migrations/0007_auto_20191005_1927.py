# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0003_auto_20190329_1522'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cpovc_forms', '0006_auto_20190329_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='OVCBasicCRS',
            fields=[
                ('case_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('case_serial', models.CharField(default=b'XXXX', max_length=50)),
                ('perpetrator_names', models.CharField(max_length=50, null=True)),
                ('child_names', models.CharField(max_length=50, null=True)),
                ('child_dob', models.DateField(default=django.utils.timezone.now)),
                ('child_sex', models.CharField(max_length=5, null=True)),
                ('perpetrator_relationship', models.CharField(max_length=50, null=True)),
                ('county', models.CharField(max_length=3)),
                ('constituency', models.CharField(max_length=3)),
                ('case_landmark', models.CharField(max_length=50, null=True)),
                ('case_category', models.CharField(max_length=5)),
                ('case_details', models.TextField(null=True)),
                ('longitude', models.DecimalField(null=True, max_digits=10, decimal_places=7)),
                ('latitude', models.DecimalField(null=True, max_digits=10, decimal_places=7)),
                ('reporter_names', models.CharField(max_length=150, null=True)),
                ('reporter_telephone', models.CharField(max_length=15, null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('account', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ovc_basic_case_record',
                'verbose_name': 'Basic Case Record',
                'verbose_name_plural': 'Basic Case Records',
            },
        ),
        migrations.AddField(
            model_name='ovccaserecord',
            name='case_stage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ovcgokbursary',
            name='date_of_issue',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='ovcgokbursary',
            name='eligibility_score',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='ovcgokbursary',
            name='father_idno',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='ovcgokbursary',
            name='mother_idno',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='ovcgokbursary',
            name='nemis',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ovcgokbursary',
            name='status_of_student',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ovcgokbursary',
            name='year_of_bursary_award',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='ovcplacement',
            name='admission_number',
            field=models.CharField(default=b'XXXX/YYYY', max_length=50),
        ),
        migrations.AddField(
            model_name='ovcplacement',
            name='residential_institution',
            field=models.ForeignKey(default=1, blank=True, to='cpovc_registry.RegOrgUnit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ovcplacement',
            name='transfer_from_institution',
            field=models.ForeignKey(related_name='ou_from', blank=True, to='cpovc_registry.RegOrgUnit', null=True),
        ),
        migrations.AddField(
            model_name='ovcplacement',
            name='transfer_to_institution',
            field=models.ForeignKey(related_name='ou_', blank=True, to='cpovc_registry.RegOrgUnit', null=True),
        ),
        migrations.AlterField(
            model_name='ovcgokbursary',
            name='application_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ovcgokbursary',
            name='approved_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ovcgokbursary',
            name='chief_recommend_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ovcgokbursary',
            name='chief_telephone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ovcgokbursary',
            name='csac_sign_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ovcgokbursary',
            name='scco_sign_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ovcgokbursary',
            name='school_bank',
            field=models.ForeignKey(to='cpovc_forms.ListBanks', null=True),
        ),
        migrations.AlterField(
            model_name='ovcgokbursary',
            name='school_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ovcgokbursary',
            name='school_recommend_date',
            field=models.DateField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0003_auto_20190329_1522'),
        ('cpovc_forms', '0007_auto_20191005_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='OVCBasicCategory',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('case_category', models.CharField(max_length=5)),
                ('case_sub_category', models.CharField(max_length=5, null=True)),
                ('case_date_event', models.DateField(default=django.utils.timezone.now)),
                ('case_nature', models.CharField(max_length=5)),
                ('case_place_of_event', models.CharField(max_length=5)),
                ('is_void', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ovc_basic_category',
                'verbose_name': 'Basic Category',
                'verbose_name_plural': 'Basic Category',
            },
        ),
        migrations.CreateModel(
            name='OVCBasicPerson',
            fields=[
                ('person_id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('relationship', models.CharField(max_length=5, null=True)),
                ('person_type', models.CharField(max_length=5, choices=[(b'PTRD', b'Reporter'), (b'PTPD', b'Perpetrator'), (b'PTCH', b'Child'), (b'PTCG', b'Guardian')])),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('other_names', models.CharField(max_length=50, null=True)),
                ('dob', models.DateField(null=True)),
                ('sex', models.CharField(max_length=5, null=True)),
                ('is_void', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ovc_basic_person',
                'verbose_name': 'Basic Person',
                'verbose_name_plural': 'Basic Persons',
            },
        ),
        migrations.CreateModel(
            name='OvcCasePersons',
            fields=[
                ('pid', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('person_relation', models.CharField(max_length=5, null=True)),
                ('person_first_name', models.CharField(max_length=100, null=True)),
                ('person_other_names', models.CharField(max_length=100, null=True)),
                ('person_surname', models.CharField(max_length=100, null=True)),
                ('person_type', models.CharField(default=b'PERP', max_length=5)),
                ('person_dob', models.DateField(null=True)),
                ('person_sex', models.CharField(max_length=4, null=True, choices=[(b'SMAL', b'Male'), (b'SFEM', b'Female')])),
                ('case', models.ForeignKey(to='cpovc_forms.OVCCaseRecord', null=True)),
                ('person', models.ForeignKey(to='cpovc_registry.RegPerson')),
            ],
            options={
                'db_table': 'ovc_case_other_person',
                'verbose_name': 'Case Other Person',
                'verbose_name_plural': 'Case Other Persons',
            },
        ),
        migrations.RenameField(
            model_name='ovcbasiccrs',
            old_name='child_dob',
            new_name='case_date',
        ),
        migrations.RenameField(
            model_name='ovcbasiccrs',
            old_name='case_details',
            new_name='case_narration',
        ),
        migrations.RenameField(
            model_name='ovcbasiccrs',
            old_name='case_category',
            new_name='case_reporter',
        ),
        migrations.RenameField(
            model_name='ovcbasiccrs',
            old_name='child_sex',
            new_name='perpetrator',
        ),
        migrations.RemoveField(
            model_name='ovcbasiccrs',
            name='child_names',
        ),
        migrations.RemoveField(
            model_name='ovcbasiccrs',
            name='perpetrator_names',
        ),
        migrations.RemoveField(
            model_name='ovcbasiccrs',
            name='perpetrator_relationship',
        ),
        migrations.RemoveField(
            model_name='ovcbasiccrs',
            name='reporter_names',
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='family_status',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='hh_economic_status',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='mental_condition',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='organization_unit',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='other_condition',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='physical_condition',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='referral',
            field=models.CharField(default=b'ANNO', max_length=5),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='referral_detail',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='reporter_county',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='reporter_sub_county',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='reporter_village',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='reporter_ward',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='risk_level',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ovcbasiccrs',
            name='summon',
            field=models.CharField(default=b'ANNO', max_length=5),
        ),
        migrations.AddField(
            model_name='ovcplacement',
            name='case_record',
            field=models.ForeignKey(blank=True, to='cpovc_forms.OVCCaseRecord', null=True),
        ),
        migrations.AddField(
            model_name='ovcbasicperson',
            name='case',
            field=models.ForeignKey(to='cpovc_forms.OVCBasicCRS'),
        ),
        migrations.AddField(
            model_name='ovcbasiccategory',
            name='case',
            field=models.ForeignKey(to='cpovc_forms.OVCBasicCRS'),
        ),
    ]

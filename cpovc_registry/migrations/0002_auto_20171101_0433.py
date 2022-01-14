# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cpovc_registry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OVCCheckin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('is_ovc', models.BooleanField(default=True)),
                ('is_void', models.BooleanField(default=False)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'ovc_checkin',
            },
        ),
        migrations.CreateModel(
            name='OVCHouseHold',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('members', models.CharField(max_length=200)),
                ('is_void', models.BooleanField(default=False)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'reg_household',
            },
        ),
        migrations.CreateModel(
            name='PersonsMaster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('person_type', models.CharField(max_length=5, null=True)),
                ('system_id', models.CharField(max_length=100, null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'reg_person_master',
            },
        ),
        migrations.CreateModel(
            name='RegBiometric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('left_iris', models.BinaryField()),
                ('right_iris', models.BinaryField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'reg_biometric',
                'verbose_name': 'Persons Biometric',
                'verbose_name_plural': 'Persons Biometrics',
            },
        ),
        migrations.AddField(
            model_name='regorgunit',
            name='handle_ovc',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='regperson',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='regperson',
            name='other_names',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personsmaster',
            name='person',
            field=models.ForeignKey(to='cpovc_registry.RegPerson', null=True),
        ),
        migrations.AddField(
            model_name='ovchousehold',
            name='index_child',
            field=models.ForeignKey(related_name='index_child', to='cpovc_registry.RegPerson'),
        ),
        migrations.AddField(
            model_name='ovccheckin',
            name='org_unit',
            field=models.ForeignKey(to='cpovc_registry.RegOrgUnit', null=True),
        ),
        migrations.AddField(
            model_name='ovccheckin',
            name='person',
            field=models.ForeignKey(to='cpovc_registry.RegPerson'),
        ),
        migrations.AddField(
            model_name='ovccheckin',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

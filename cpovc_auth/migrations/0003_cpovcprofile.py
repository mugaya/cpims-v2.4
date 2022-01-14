# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_auth', '0002_auto_20160812_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPOVCProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('details', models.TextField(default=b'{}')),
                ('is_void', models.BooleanField(default=False)),
                ('timestamp_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_user_profile',
            },
        ),
    ]

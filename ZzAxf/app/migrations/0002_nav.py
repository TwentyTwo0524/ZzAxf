# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
    ]

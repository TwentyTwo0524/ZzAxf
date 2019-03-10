# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_mainshow_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodtype',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('typeid', models.CharField(max_length=10)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]

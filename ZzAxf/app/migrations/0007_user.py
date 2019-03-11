# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('email', models.CharField(unique=True, max_length=40)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=40, default='axf.png')),
                ('rank', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]

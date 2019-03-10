# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainshow',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('trackid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('categoryid', models.CharField(max_length=10)),
                ('brandname', models.CharField(max_length=100)),
                ('img1', models.CharField(max_length=100)),
                ('childcid1', models.CharField(max_length=10)),
                ('productid1', models.CharField(max_length=10)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.CharField(max_length=10)),
                ('marketprice1', models.CharField(max_length=10)),
                ('img2', models.CharField(max_length=100)),
                ('childcid2', models.CharField(max_length=10)),
                ('productid2', models.CharField(max_length=10)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=10)),
                ('marketprice2', models.CharField(max_length=10)),
                ('img3', models.CharField(max_length=100)),
                ('childcid3', models.CharField(max_length=10)),
                ('productid3', models.CharField(max_length=10)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=10)),
                ('marketprice3', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]

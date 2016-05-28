# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_user_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default=b'Email', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]

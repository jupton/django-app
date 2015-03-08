# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='reporter',
            field=models.CharField(default='', max_length=100, choices=[(b'Clark Kent', b'Clark Kent'), (b'Lois Lane', b'Lois Lane')]),
            preserve_default=False,
        ),
    ]

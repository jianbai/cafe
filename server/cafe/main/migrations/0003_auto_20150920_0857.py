# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_hasreviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='user1review',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='user2review',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

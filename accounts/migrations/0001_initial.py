# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(primary_key=True, max_length=254, serialize=False)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

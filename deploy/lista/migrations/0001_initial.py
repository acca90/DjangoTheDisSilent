# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=True,
        ),
    ]

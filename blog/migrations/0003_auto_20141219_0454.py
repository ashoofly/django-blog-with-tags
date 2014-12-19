# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('blog', '0002_auto_20141219_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', to='taggit.Tag', help_text='A comma-separated list of tags.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(editable=False),
            preserve_default=True,
        ),
    ]

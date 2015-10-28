# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisualGraph', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arcmodel',
            name='a',
        ),
        migrations.RemoveField(
            model_name='arcmodel',
            name='b',
        ),
        migrations.RemoveField(
            model_name='graphmodel',
            name='arcs',
        ),
        migrations.RemoveField(
            model_name='graphmodel',
            name='nodes',
        ),
        migrations.AddField(
            model_name='graphmodel',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ArcModel',
        ),
        migrations.DeleteModel(
            name='NodeModel',
        ),
    ]

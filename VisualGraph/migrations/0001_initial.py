# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArcModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GraphModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('arcs', models.ManyToManyField(to='VisualGraph.ArcModel')),
            ],
        ),
        migrations.CreateModel(
            name='NodeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('number', models.IntegerField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='graphmodel',
            name='nodes',
            field=models.ManyToManyField(to='VisualGraph.NodeModel'),
        ),
        migrations.AddField(
            model_name='arcmodel',
            name='a',
            field=models.ForeignKey(related_name='a', to='VisualGraph.NodeModel'),
        ),
        migrations.AddField(
            model_name='arcmodel',
            name='b',
            field=models.ForeignKey(related_name='b', to='VisualGraph.NodeModel'),
        ),
    ]

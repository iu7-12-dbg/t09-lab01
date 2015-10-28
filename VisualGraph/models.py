from django.db import models
from graph.graph import *

# Create your models here.

#
# class NodeModel(models.Model):
#     number = models.IntegerField()
#     x = models.FloatField()
#     y = models.FloatField()
#
#
# class ArcModel(models.Model):
#     a = models.ForeignKey(NodeModel, related_name='a')
#     b = models.ForeignKey(NodeModel, related_name='b')
#     weight = models.FloatField()


class GraphModel(models.Model):
    # arcs = models.ManyToManyField(ArcModel)
    # nodes = models.ManyToManyField(NodeModel)
    text = models.TextField()


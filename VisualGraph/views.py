from django.shortcuts import render, HttpResponse, Http404
from django.template import RequestContext, loader
from django.views.generic import View
from VisualGraph.models import *
from graph.astar import *
from graph.graph import *
import json


"""
    Не обращайте внимания на это говно, будем просто в виде текста хранить
"""


class GraphView:
    @staticmethod
    def get(request, pk, *args, **kwargs):
        try:
            obj = GraphModel.objects.get(id=pk)
            res = obj.text
            return HttpResponse(res)
        except:
            raise Http404()

    @staticmethod
    def post(request, *args, **kwargs):
        """
            {"arcs": [{"a": 0, "b": 1, "w": 10},...], "nodes": [{"value": 0, "x": 10, "y":5},...]}
        """
        s = request.body.decode()
        a = json.loads(s)
        if 'nodes' not in a.keys() or 'arcs' not in a.keys():
            raise Exception()
        gr = GraphModel(text=s)
        gr.save()
        return HttpResponse(':'.join(['id', str(gr.id)]))


def solve_graph(request, pk, a, b):
        text = GraphModel.objects.get(id=pk).text
        g = graph_from_text(text)
        ast = AStar(g)
        a, b = int(a), int(b)
        a = getNode(g.nodes(), a)
        b = getNode(g.nodes(), b)
        res = ast.start(a, b)
        res = json.dumps(res)
        return HttpResponse(res)


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))

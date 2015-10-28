from django.shortcuts import render, HttpResponse, Http404
from django.template import RequestContext, loader
from django.views.generic import View
from VisualGraph.models import *
from graph.astar import *
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
            # я заебался, хз что за ошибка
            a = json.loads(str(request.body))
            if not hasattr(a, 'nodes') or not hasattr(a, 'arcs'):
                raise Exception()
            gr = GraphModel(text=request.body)
            gr.save()
            return HttpResponse(':'.join(['id', str(gr.id)]))


def solve_graph(request, pk, a, b):
    try:
        obj = GraphModel.objects.get(id=pk).text
        obj = json.loads(obj)
        nodes = getattr(obj, 'nodes')
        arcs = getattr(obj, 'arcs')
        g = Graph(nodes, arcs)
        ast = AStar(g)
        res = ast.start(a, b)
        res = json.dumps(res)
        return HttpResponse(res)
    except:
        raise Http404('NO')


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))

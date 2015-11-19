from django.shortcuts import render, Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from VisualGraph.models import *
from graph.astar import *
from graph.graph import *
import json
import logging


logger = logging.getLogger('views')


class GraphView:
    @staticmethod
    def get(request, pk, *args, **kwargs):
        logger.info("requesting graph with pk: " + str(pk))

        try:
            obj = GraphModel.objects.get(id=pk)

            logger.info("graph: " + str(obj))

            context = {'graph': obj.text, 'pk': pk}

            logger.info("context for response: " + str(context))

            return render(request, 'graph/index.html', context)
        except:
            logger.info("graph has not been found")
            raise Http404()

    @staticmethod
    def post(request, *args, **kwargs):
        """
            {"arcs": [{"a": 0, "b": 1, "w": 10},...], "nodes": [{"value": 0, "x": 10, "y":5},...]}
        """

        logger.info("Request graph: " + str(request.POST.dict()))

        text = request.POST.get('graph', '')

        logger.info("Request graph: '" + text + "'")

        # graphJSON = json.loads(text)

        # logger.info("graph JSON: " + graphJSON)

        # if graphJSON is not '' or 'nodes' not in graphJSON.keys() or 'arcs' not in graphJSON.keys():
        #     raise Exception("Bad graph JSON")

        gr = GraphModel(text=text)
        gr.save()

        logger.info("graph saved, pk: " + str(gr.pk))

        return HttpResponse('{' + ':'.join(['id', str(gr.id)]) + '}')


def solve_graph(request, pk, a, b):
        logger.info("Requested solution for graph (pk = " + str(pk) + ") from " + str(a) + " to " + str(b))

        text = GraphModel.objects.get(id=pk).text

        logger.debug("Graph JSON is: " + str(text))

        g = graph_from_text(text)

        logger.debug("Graph object for A*: " + str(g))

        ast = AStar(g)
        a, b = int(a), int(b)
        a = getNode(g.nodes(), a)
        b = getNode(g.nodes(), b)
        res = ast.start(a, b)

        logger.info("Result from A*: " + str(res))

        res = json.dumps(res)

        logger.info("Resulting JSON: " + res)

        return HttpResponse(res)


def index(request):
    template = loader.get_template('graph/index.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))

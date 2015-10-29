from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^graph/(?P<pk>[0-9]+)/$', views.GraphView.get, name='graph'),
    url(r'^graph$', views.GraphView.post, name='graph'),
    url(r'^graph/solve/(?P<pk>[0-9]+)/(?P<a>[0-9]+)/(?P<b>[0-9]+)/$', views.solve_graph, name='solve')
]

import networkx as nx
from PageRank import PageRank
from werkzeug.datastructures import MultiDict

PageRank = PageRank()
graph = MultiDict([('sources-1', '1-2'), ('sources-2', '3'), ('sources-3', '2-3')])
PageRank.PageRank_networkx(graph, e=10e-6, lamb=0.85)
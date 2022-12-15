import numpy as np
from numpy.linalg import norm
from more_itertools import locate
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from werkzeug.datastructures import MultiDict


class PageRank:
    def PageRank_TP(self, TP, e=10e-6, lamb=0.85):
        print('TM')
        N = len(TP)
        R0 = np.ones(N) * (1 / N)
        l = 0

        R = R0
        while (True):
            R_prev = R
            R = np.dot(R_prev, TP)
            if (norm(R - R_prev, ord=1) < e):
                return np.round_(R * 100, 2)

    def PageRank_adjacency_matrix(self, AM, e=10e-6, lamb=0.85):
        print('AM')
        N = len(AM)
        P = list()
        for row in AM:
            sum_Aij = np.sum(row)
            if sum_Aij != 0:
                Pi = lamb * (row / sum_Aij) + (1 - lamb) / N
                P.append(Pi)
            else:
                Pi = 1 / N * np.ones(N)
                P.append(Pi)

        R_final = PageRank.PageRank_TP(self, P, e=e, lamb=lamb)
        print(R_final)
        AM = np.array(AM)
        sources = list()
        targets = list()
        for i, row in enumerate(AM):
            if row.sum() != 0:
                # print(row)
                for j, elem in enumerate(row):
                    if elem == 1:
                        sources.append(i + 1)
                        targets.append(j + 1)

        print(f'sources: {sources}')
        print(f'sources: {targets}')
        G = nx.DiGraph()
        # print(f'unique {np.unique(sources)}')
        G.add_nodes_from(np.unique(sources))
        relationships = pd.DataFrame({'from': sources,
                                      'to': targets})
        G = nx.from_pandas_edgelist(relationships, 'from', 'to', create_using=nx.DiGraph())

        PageRank.draw_graph(self, G, R_final)

        return np.round_(R_final, 4)

    def PageRank_graphMl(self, graph, e=10e-6, lamb=0.85):
        print('graph')
        nodes = graph.getElementsByTagName('node')
        edges = graph.getElementsByTagName('edge')

        print(f'{nodes.length} nodes')
        print(f'{edges.length} links')

        sources = list()
        targets = list()
        for edge in edges:
            source = edge.getAttribute('source')
            sources.append(int(source))
            target = edge.getAttribute('target')
            targets.append(int(target))


        unique_sources = np.unique(sources)
        AM = list()
        for i in range(1, nodes.length + 1):

            if i in unique_sources:
                row = np.zeros(nodes.length, dtype=int).tolist()
                indices = locate(sources, lambda x: x == i)
                indices = list(indices)

                for i in indices:
                    row[targets[i] - 1] = 1

                AM.append(row)
            else:
                AM.append(np.zeros(nodes.length, dtype=int).tolist())

        R_final = PageRank.PageRank_adjacency_matrix(self, AM, e=e, lamb=lamb)

        return np.round_(R_final, 4)

    def PageRank_networkx(self, graph, e=10e-6, lamb=0.85):
        print('Graph Object')

        sources = list()
        targets = list()
        for i in range(1, len(graph) + 1):
            targets_i = graph[f'sources-{i}']
            targets_i = targets_i.split('-')
            targets += targets_i
            num_targets_i = len(targets_i)

            sources_i = (i * np.ones(num_targets_i, dtype=int)).tolist()
            sources += sources_i


        targets = [eval(x) if x != '' else 0 for x in targets]
        print(f'source {sources}\ntargets {targets}')

        G = nx.DiGraph()
        # print(f'unique {np.unique(sources)}')
        G.add_nodes_from(np.unique(sources))

        # for i, j in zip(sources, targets):
        #     if j != 0:
        #         G.add_edge(i, j)


        relationships = pd.DataFrame({'from': sources,
                                      'to': targets})
        G = nx.from_pandas_edgelist(relationships, 'from', 'to', create_using=nx.DiGraph())

        AM = nx.adjacency_matrix(G).todense()
        AM = np.array(AM)
        print(AM)
        R_final = PageRank.PageRank_adjacency_matrix(self, AM, e=e, lamb=lamb)

        print(f'R_final {R_final}')

        PageRank.draw_graph(self, G, R_final)

        return np.round_(R_final, 4)


    def draw_graph(self, graph, ranks):
        plt.subplots(figsize=(15, 10))
        node_sizes = np.dot(200, ranks)
        nx.draw_circular(graph, with_labels=True, node_size=node_sizes, width=3, font_size=30)

        plt.savefig('./static/images/graph.png', format='png')
        print('saved!')
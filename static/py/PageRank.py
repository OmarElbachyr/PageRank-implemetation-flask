import pandas as pd
import numpy as np
from numpy.linalg import norm
from more_itertools import locate
import networkx as nx
import matplotlib.pyplot as plt


class PageRank:
    def PageRank_TP(self, TP, e=10e-6, lamb=0.85):
        print('TM')
        N = 11
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
        N = 11
        P = list()
        for row in AM:
            sum_Aij = np.sum(row)
            if sum_Aij != 0:
                Pi = lamb * (row / sum_Aij) + (1 - lamb) / N
                P.append(Pi)
            else:
                Pi = 1 / N * np.ones(N)
                P.append(Pi)

        R_final = PageRank.PageRank_TP(self, P, e=10e-6, lamb=0.85)

        return np.round_(R_final, 4)

    def PageRank_graphMl(self, graph, e=10e-6, lamb=0.85):
        print('graph')
        nodes = graph.getElementsByTagName('node')
        edges = graph.getElementsByTagName('edge')

        print(f'{nodes.length} nodes')
        print(f'{edges.length} links')
        # for node in nodes:
        #     print(node.getAttribute('id'))

        sources = list()
        targets = list()
        for edge in edges:
            source = edge.getAttribute('source')
            sources.append(int(source))
            target = edge.getAttribute('target')
            targets.append(int(target))
            # print(f'source: {source}, targets: {target}')

        unique_sources = np.unique(sources)
        AM = list()
        for i in range(1, nodes.length + 1):
            # print(i)
            if i in unique_sources:
                row = np.zeros(nodes.length, dtype=int).tolist()
                indices = locate(sources, lambda x: x == i)
                indices = list(indices)

                for i in indices:
                    row[targets[i] - 1] = 1

                # print(row)
                AM.append(row)
            else:
                AM.append(np.zeros(nodes.length, dtype=int).tolist())

        R_final = PageRank.PageRank_adjacency_matrix(self, AM, e=10e-6, lamb=0.85)

        return np.round_(R_final, 4)


    def PageRank_networkx(self, e=10e-6, lamb=0.85):
        print('Graph Object')
        G = nx.DiGraph()

        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        G.add_edge(2, 3)
        G.add_edge(3, 2)
        G.add_edge(4, 1)
        G.add_edge(4, 2)
        G.add_edge(5, 2)
        G.add_edge(5, 4)
        G.add_edge(5, 6)
        G.add_edge(6, 2)
        G.add_edge(6, 5)
        G.add_edge(7, 2)
        G.add_edge(7, 5)
        G.add_edge(8, 2)
        G.add_edge(8, 5)
        G.add_edge(9, 2)
        G.add_edge(9, 5)
        G.add_edge(10, 5)
        G.add_edge(11, 5)

        AM = nx.adjacency_matrix(G).todense().tolist()
        # print(type(AM))
        # print(AM)
        R_final = PageRank.PageRank_adjacency_matrix(self, AM, e=10e-6, lamb=0.85)
        print(R_final)
        return np.round_(R_final, 4)

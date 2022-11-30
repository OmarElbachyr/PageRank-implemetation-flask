import pandas as pd
import numpy as np
from numpy.linalg import norm

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
                return R

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

        return R_final
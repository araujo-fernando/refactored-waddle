from typing import List

from .utilities import *
from .vertex import Vertex

class CompleteUndirectedGraph:
    def __init__(self, vertexes: List[Vertex]):
        self.V = vertexes
        self.edges = list()
 
        self._compute_edges()
        self.edges = sorted(self.edges, key=lambda item: item[2])

    def _compute_edges(self):
        for idx, u in enumerate(self.V):
            for v in self.V[idx + 1:]:
                edge = [u, v, compute_distance(u, v)]
                self.edges.append(edge)

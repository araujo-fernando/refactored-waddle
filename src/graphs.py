from typing import List, NamedTuple

from .utilities import *
from .vertex import Vertex


class Edge(NamedTuple):
    u: Vertex
    v: Vertex
    w: float

class UndirectedGraph:
    def __init__(self, vertexes: List[Vertex], edges: List[Edge] | None = None) -> None:
        self.V = vertexes
        self.edges = edges if edges is not None else list()

    @property
    def is_connected(self) -> bool:
        return len(self.find_vertexes_connected_to_vertex(self.V[0])) == len(self.V) - 1

    def copy(self):
        copy = self.__new__(UndirectedGraph)
        copy.V = self.V.copy()
        copy.edges = self.edges.copy()

        return copy
    
    def find_vertexes_with_degree(self, degree: int):
        vertex_degrees = {v: 0 for v in self.V}
        for edge in self.edges:
            vertex_degrees[edge.u] += 1
            vertex_degrees[edge.v] += 1
        
        return [v for v in vertex_degrees if vertex_degrees[v] == degree]
    
    def find_egdes_of_vertex(self, vertex: Vertex):
        return [e for e in self.edges if vertex in e]

    def find_vertexes_connected_to_vertex(self, vertex: Vertex) -> set[Vertex]:
        vertexes = set()
        for edge in self.edges:
            if vertex == edge.u:
                vertexes.add(edge.v)
            elif vertex == edge.v:
                vertexes.add(edge.u)

        return vertexes

class CompleteUndirectedGraph(UndirectedGraph):
    def __init__(self, vertexes: List[Vertex]) -> None:
        self.V = vertexes
        self.edges: list[Edge] = list()

        self._compute_edges()
        self.edges = sorted(self.edges, key=lambda item: item[2])

    def _compute_edges(self):
        for idx, u in enumerate(self.V):
            for v in self.V[idx + 1 :]:
                edge = Edge(u, v, compute_distance(u, v))
                self.edges.append(edge)

    def copy(self):
        copy = self.__new__(CompleteUndirectedGraph)
        copy.V = self.V.copy()
        copy.edges = self.edges.copy()

        return copy
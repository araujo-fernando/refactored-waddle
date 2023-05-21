from .graphs import CompleteUndirectedGraph
from .utilities import *

def kruskal(graph: CompleteUndirectedGraph):
    f = []
    sets = [{v} for v in graph.V]

    for u, v, w in graph.edges:
        set_u = find_set(sets, u)
        set_v = find_set(sets, v)

        if set_u != set_v:
            f.append([u, v, w])
            sets.remove(set_v)
            sets.remove(set_u)
            sets.append(set_u.union(set_v))

    return f

def prim(graph: CompleteUndirectedGraph):
    f = []
    Q = graph.V.copy()

    u = Q.pop(0)
    v = find_closest_vertex(Q, u)
    f.append([u, v, compute_distance(u, v)])
    selected_vertexes = {u, v}
    Q.remove(v)

    while len(Q) > 0:
        u, v = find_closest_vertex_to_subset(Q, selected_vertexes)
        f.append([u, v, compute_distance(u, v)])
        Q.remove(v)
        selected_vertexes.add(v)

    return f
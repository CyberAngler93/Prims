# Simple python prims algorithm
# Created by Matt Perry on 12/02/202
# Last Modified 12/02/20
# For CS411 HW 7
# Prof. Hartman Fall 2020
import heapq
from collections import defaultdict


def prims(graph, root_vertex) -> dict:
    min_span_tree = defaultdict(list)
    is_visited = {root_vertex}
    # generate list of tuples that contain cost, root, next_vertex
    edges = []
    for next_vertex, cost in graph[root_vertex].items():
        edges.append((cost, root_vertex, next_vertex))
    # Put root edges into priority queue
    heapq.heapify(edges)
    while edges:
        cost, current_vertex, next_vertex = heapq.heappop(edges)
        if next_vertex not in is_visited:
            is_visited.add(next_vertex)
            min_span_tree[current_vertex].append(next_vertex)
            for to_next_node, cost, in graph[next_vertex].items():
                if to_next_node not in is_visited:
                    heapq.heappush(edges, (cost, next_vertex, to_next_node))
    return dict(min_span_tree)

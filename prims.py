# Simple python prims algorithm
# Created by Matt Perry on 12/02/202
# Last Modified 12/12/20
# For CS411 HW 7
# Prof. Hartman Fall 2020
import heapq
import fibheap
from collections import defaultdict


def fib_heap_prims(graph, root_vertex) -> dict:
    min_span_tree = defaultdict(list)
    is_visited = {root_vertex}
    # generate list of tuples that contain cost, root, next_vertex
    edges = []
    for next_vertex, cost in graph[root_vertex].items():
        edges.append((cost, root_vertex, next_vertex))
    # Put root edges into priority queue
    fib_heap = fibheap.makefheap()
    for item in edges:
        fibheap.fheappush(fib_heap, item)
    while fib_heap.num_nodes:
        (cost, current_vertex, next_vertex) = fibheap.fheappop(fib_heap)
        if next_vertex not in is_visited:
            is_visited.add(next_vertex)
            min_span_tree[current_vertex].append(next_vertex)
            for to_next_node, cost, in graph[next_vertex].items():
                if to_next_node not in is_visited:
                    fibheap.fheappush(fib_heap, (cost, next_vertex, to_next_node))
    return dict(min_span_tree)


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

# Simple python prims algorithm
# Created by Matt Perry on 12/02/202
# Last Modified 12/02/20
# For CS411 HW 7
# Prof. Hartman Fall 2020
import heapq
from collections import defaultdict


def prims(graph, root) -> dict:
    min_span_tree = defaultdict(set)
    is_visited = {root}
    # generate edges that leave the root node
    edges = [
        (cost, root, next_node)
        for next_node, cost in graph[root].items()
    ]
    # Put root edges into priority queue
    heapq.heapify(edges)
    while edges:
        cost, current_node, next_node = heapq.heappop(edges)
        if next_node not in is_visited:
            is_visited.add(next_node)
            min_span_tree[current_node].add(next_node)
            for to_next_node, cost, in graph[next_node].items():
                if to_next_node not in is_visited:
                    heapq.heappush(edges, (cost, next_node, to_next_node))

    return dict(min_span_tree)

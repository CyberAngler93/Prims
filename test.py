# Test suite for my implementation of Prims Minimum Spanning Tree
# Created by Matt Perry on 12/02/20
# Last Modified 12/12/20
# For CS411 HW7
# Prof. Hartman Fall 2020
import prims


def check_fib(example, root_vertex, result):
    res = prims.fib_heap_prims(example, root_vertex)
    if res != result:
        print(f"Failed!")
        print(f"Expected = {result}\nBut got:\nResult   = {prims.fib_heap_prims(example, root_vertex)}\n")
    else:
        print("OK!")


def check(example, root_vertex, result):
    res = prims.prims(example, root_vertex)
    if res != result:
        print(f"Failed!")
        print(f"Expected = {result}\nBut got:\nResult   = {prims.prims(example, root_vertex)}\n")
    else:
        print("OK!")


def test():
    example_graph_medium = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 4, 'D': 2, 'E': 3},
    'C': {'A': 1, 'B': 4, 'F': 1},
    'D': {'B': 2, 'E': 1, 'G': 2},
    'E': {'B': 3, 'D': 1, 'F': 2},
    'F': {'C': 1, 'E': 2},
    'G': {'D': 2, 'F': 1},
    }
    example_graph_medium_result_a = {
        'A': ['C'],
        'C': ['F'],
        'F': ['E'],
        'E': ['D'],
        'D': ['B', 'G'],
    }
    example_graph_medium_result_b = {
        'B': ['D'],
        'D': ['E', 'G'],
        'G': ['F'],
        'F': ['C'],
        'C': ['A'],
    }
    example_graph_small = {
        'A': {'B': 2},
        'B': {'A': 2},
    }
    example_graph_small_result_a = {
        'A': ['B']
    }
    example_graph_small_result_b = {
        'B': ['A']
    }
    example_only_root = {
        'A': {'A': '1'},
    }
    example_only_root_result = {}
    print('Starting fibheap tests')
    print('Starting Tiny Graph Test Suite')
    print('Testing a Single Vertex')
    check_fib(example_only_root, 'A', example_only_root_result)

    print('Starting Small Test Suite')
    print('Testing Small Start at node A')
    check_fib(example_graph_small, 'A', example_graph_small_result_a)
    print('Testing Small Start at node B')
    check_fib(example_graph_small, 'B', example_graph_small_result_b)

    print('Starting Medium Test Suite')
    print('Testing Medium Starting at node A')
    check_fib(example_graph_medium, 'A', example_graph_medium_result_a)
    print('Testing Medium Starting at node B')
    check_fib(example_graph_medium, 'B', example_graph_medium_result_b)
    print('Tests Completed')

    print('Starting heapq tests')
    print('Starting Tiny Graph Test Suite')
    print('Testing a Single Vertex')
    check(example_only_root, 'A', example_only_root_result)

    print('Starting Small Test Suite')
    print('Testing Small Start at node A')
    check(example_graph_small, 'A', example_graph_small_result_a)
    print('Testing Small Start at node B')
    check(example_graph_small, 'B', example_graph_small_result_b)

    print('Starting Medium Test Suite')
    print('Testing Medium Starting at node A')
    check(example_graph_medium, 'A', example_graph_medium_result_a)
    print('Testing Medium Starting at node B')
    check(example_graph_medium, 'B', example_graph_medium_result_b)
    print('Tests Completed')


if __name__ == "__main__":
    test()

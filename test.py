# Test suite for my implementation of Prims Minimum Spanning Tree
# Created by Matt Perry on 12/02/20
# Last Modified 12/02/20
# For CS411 HW7
# Prof. Hartman Fall 2020
import prims


def test():
    fail = False
    example_graph_medium = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 4, 'D': 2, 'E': 3},
    'C': {'A': 1, 'B': 4, 'F': 1},
    'D': {'B': 2, 'E': 1, 'G': 2},
    'E': {'B': 3, 'D': 1, 'F': 2},
    'F': {'C': 1, 'E': 2},
    'G': {'D': 2, 'F': 1},
    }
    example_graph_medium_result_A = {
        'A': ['C'],
        'C': ['F'],
        'F': ['E'],
        'E': ['D'],
        'D': ['B', 'G'],
    }
    example_graph_medium_result_B = {
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
    example_graph_small_result_A = {
        'A': ['B']
    }
    example_graph_small_result_B = {
        'B': ['A']
    }
    example_only_root = {
        'A': {'A': '1'},
    }
    example_only_root_result = {}

    print('Starting Tiny Graph Test Suite')
    print('Testing a Single Vertex')
    print(f"Expected = {example_only_root_result}\nResult   = {prims.prims(example_only_root, 'A')}\n")
    if prims.prims(example_only_root, 'A') != example_only_root_result:
        print("failed")
        fail = True
    print("Starting Small Test Suite")
    print('Testing Small Start at node A')
    print(f"Expected = {example_graph_small_result_A}\nResult   = {prims.prims(example_graph_small, 'A')}")
    if prims.prims(example_graph_small, 'A') != example_graph_small_result_A:
        print("failed")
        fail = True
    print('Testing Small Start at node B')
    print(f"Expected = {example_graph_small_result_B}\nResult   = {prims.prims(example_graph_small, 'B')}\n")
    if prims.prims(example_graph_small, 'B') != example_graph_small_result_B:
        print("failed")
        fail = True
    print("Starting Medium Test Suite")
    print('Testing Medium Starting at node A')
    print(f"Expected = {example_graph_medium_result_A}\nResult   = {prims.prims(example_graph_medium, 'A')}")
    if prims.prims(example_graph_medium, 'A') != example_graph_medium_result_A:
        print("failed")
        fail = True
    print('Testing Medium Starting at node B')
    print(f"Expected = {example_graph_medium_result_B}\nResult   = {prims.prims(example_graph_medium, 'B')}\n")
    if prims.prims(example_graph_medium, 'B') != example_graph_medium_result_B:
        print("failed")
        fail = True
    if fail:
        print('Tests Completed With Failure')
    else:
        print('Test Completed and Passing All!')


if __name__ == "__main__":
    test()

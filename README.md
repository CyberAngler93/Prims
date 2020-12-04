# Prims
 This repository is my implementation of Prim's Algorithm in Python3.  
 The purpose is to fulfill requirements for CS411 HW#7 Fall 2020.
 
 ## Assignment
 
 The Assignment is to implement an algorithm of choice.  
 
 ## Method
 
 This implementation utilizes the heapq python lib to store the tuples of the edges that are described by the cost, root_vertex, and next_vertex; in a priority queue based on cost.
 Once the root_vertex edges are generated they are placed in the queue with ``heapq.heapify``  Then all the edges are traversed and a minimum spanning tree is generated.  
 
 ## Usage
 
 How to use ``prims`` function is by including ``prims.py`` in your file and calling ``prims.prims(graph, root_vertex)`` 
 
 How to use ``fib_heap_prims`` function is by including ``prims.py`` in your file and calling ``prims.fib_heap_prims(graph, root_vertex)`` 
 
 
 ### Type Requirements
 
 ``graph`` must be a dictionary representation of the graph in which each vertex is described by a dictionary of vertices and costs.  
 for example a graph can be described as follows: ``{'A': {'A': 1, 'B': 3}, 'B': {'A': 3}}``  
 ``root_vertex`` must be a value that exists in the provide graph description. 
 
 ## Test 
 
 This project contains a simple test suite written to confirm the functionality of the algorithm utilizing both the fibheap and heapq. These tests are included in the ``test.py``
 
 ## Things that can be improved
 
 The test suite does not utilize a testing framework and would likely be a good place to improve on. 
 
 
 ## Analysis 
 
 According to heapq documentation heapfy is a linear in place operation [source](https://docs.python.org/3/library/heapq.html#heapq.heapify)  
 heapq also is implemented using a basic binary heap, I wanted to know if a Fibonacci Heap would perform better on prims with python.
 
 A Fibonacci Heap python [lib](https://pypi.org/project/fibheap/), a second iteration was prims was made utilizing a fibheap. 
 
 ### Timing
 
 Coming soon timing comparison between heapq and fibheap.
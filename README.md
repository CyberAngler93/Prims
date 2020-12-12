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
 
 ## Timing
A new timing suite was added utilizing a large random graph builder. This will generate a graph with 52 vertices with a random number of edges, with weight between 0 and 5. 

The graph is then ran through prims on both the heapq and fibq methods utilizing python ``time.time()`` . 

### Results

The results of the timing experiments found that the heapq method ran faster than the fibq method. 

Here are the results after 5 runs:  
heapq:0.001985788345336914  
fibq--::0.0689995288848877

heapq:0.0010004043579101562  
fibq--::0.069000244140625

heapq:0.0009999275207519531  
fibq--::0.08899807929992676

heapq:0.001994609832763672  
fibq--::0.07899713516235352

heapq:0.0009925365447998047  
fibq--::0.0800015926361084

### Thoughts

I orignially expected a fibheap to perform better and was concerned that maybe the libary that I am using was bad. I was able to find some others finding the same results in pythong. I found this github [repository](https://github.com/danielborowski/fibonacci-heap-python) talking about a similar finding. 

I was suprised to find some interesting talk on a stack overflow about this [topic](https://stackoverflow.com/questions/504823/has-anyone-actually-implemented-a-fibonacci-heap-efficiently/508221#508221) as well.

### Conclusion

Further testing should be done, as after reading some peopels thoughts about the topic its possible that a different implementation of fibq could be needed. It should be worth noting that I was unable to get any real time to either function before pushing the vertex count around the 50s and doing 1000 rounds of random edge adding. Although becuase of how python dictionaries work duplicate edges were replaces with a new value. 

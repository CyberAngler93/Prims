# timing suite for my implementation of Prims Minimum Spanning Tree
# Created by Matt Perry on 12/12/20
# Last Modified 12/12/20
# For CS411 HW7
# Prof. Hartman Fall 2020
import prims
import time
import random


# gengraph will build a random legal graph, it will then call the two versions of prims, fib and heapq and print results
def gengraph():
    graph = {}
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in letters:
        graph[letter] = {}
    count = 0
    while count < 10000:
        one = random.choice(letters)
        two = random.choice(letters)
        num = random.randrange(0, 5)
        graph[one][two] = num
        graph[two][one] = num
        count += 1
    print(graph)
    vertex = random.choice(letters)
    start = time.time()
    res = prims.prims(graph, vertex)
    heapqtime = time.time() - start
    print(res)
    print(f'heapq:{heapqtime}')
    start = time.time()
    res = prims.fib_heap_prims(graph, vertex)
    fibqtime = time.time() - start
    print(f'fibq: {fibqtime}')


if __name__ == "__main__":
    gengraph()
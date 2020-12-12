import prims
import time
import random

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
    print(heapqtime)
    start = time.time()
    res = prims.fib_heap_prims(graph, vertex)
    fibqtime = time.time() - start
    print(res)
    print(fibqtime)


if __name__ == "__main__":
    gengraph()
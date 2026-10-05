#BFS (Breadth First Search) explores nodes level by level.

#Step 1 : Import Deque Modeule 
from collections import deque

#Step 2 : Make  a Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}


#Step 3 : An empty visited set which will be storing Visited nodes
visited = set()

#Step 4 : We will make a queue 
queue = deque(['A'])


#Step 5 : We will write a while function 
while queue:
    node = queue.popleft()
    
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        
        for neighbour in graph[node]:
            queue.append(neighbour)
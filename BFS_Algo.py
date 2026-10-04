#BFS (Breadth First Search) explores nodes level by level.

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

visited = set()

queue = deque(['A'])

while queue:
    node = queue.popleft()
    
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        
        for neighbour in graph[node]:
            queue.append(neighbour)
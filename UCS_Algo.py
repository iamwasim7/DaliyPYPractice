#Uniform Cost Search (UCS) always expands the node with the lowest total path cost

import heapq

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 3)],
    'C': [('D', 1)],
    'D': []
}

queue = [(0, 'A')]
visited = set()

while queue:
    cost, node = heapq.heappop(queue)

    if node in visited:
        continue

    visited.add(node)
    print(node, "Cost:", cost)

    for neighbour, edge_cost in graph[node]:
        if neighbour not in visited:
            heapq.heappush(queue, (cost + edge_cost, neighbour))
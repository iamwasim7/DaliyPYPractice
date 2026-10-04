#DFS (Depth First Search) is a graph traversal algorithm that explores a path as deeply as possible before backtracking.


#Step 1 : Make a Graph
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []
}

#Step 2 : An empty set to store visited node
visited = set()

#Step 3 : An Function dfs 

def dfs(node):
    if node not in visited:
        print(node, end=" ")  #This prints the current node
        visited.add(node)     #Adding the node to visited
        
        for neighbour in graph[node]:          #Take each neighbour connected to the current node, one by one
            dfs(neighbour)                     #It calls the same DFS function again for the neighbour.
            
dfs('A')                                       #Start DFS from node A.
        


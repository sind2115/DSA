def dfs(graph, start, visited):
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def initialize_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        edge_info = input("Enter edge information (start_vertex end_vertex), separated by space: ").split()
        start_vertex, end_vertex = edge_info

        if start_vertex not in graph:
            graph[start_vertex] = []
        if end_vertex not in graph:
            graph[end_vertex] = []

        graph[start_vertex].append(end_vertex)
        graph[end_vertex].append(start_vertex)

    return graph

graph = initialize_graph()
start_vertex = input("Enter the start vertex for DFS: ")

visited_nodes = set()
print("DFS traversal starting from vertex", start_vertex, ":")
dfs(graph, start_vertex, visited_nodes)

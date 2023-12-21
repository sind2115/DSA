def init_graph():
    n = int(input("Enter the number of vertices: "))
    graph = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
    
    m = int(input("Enter the number of edges: "))
    
    for _ in range(m):
        edge_info = input("Enter edge info (start_vertex end_vertex weight), separated by space: ").split()
        start, end, weight = map(int, edge_info)
        graph[start - 1][end - 1] = weight
    
    return graph

def floyd_algorithm(g):
    n = len(g)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

def display_result(g):
    print("Shortest distances between vertices:")
    for row in g:
        print(row)

graph = init_graph()
floyd_algorithm(graph)
display_result(graph)

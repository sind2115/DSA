from collections import deque

def bfs(g, s):
    visited = set()
    q = deque([s])
    visited.add(s)

    while q:
        cv = q.popleft()
        print(cv, end=" ")

        for n in g[cv]:
            if n not in visited:
                q.append(n)
                visited.add(n)

def init_graph():
    g = {}
    m = int(input("Enter the number of edges: "))

    for _ in range(m):
        edge_info = input("Enter edge info (start_vertex end_vertex), separated by space: ").split()
        sv, ev = edge_info

        if sv not in g:
            g[sv] = []
        if ev not in g:
            g[ev] = []

        g[sv].append(ev)
        g[ev].append(sv)

    return g

graph = init_graph()
start_vertex = input("Enter the start vertex for BFS: ")

print("BFS traversal starting from vertex", start_vertex, ":")
bfs(graph, start_vertex)

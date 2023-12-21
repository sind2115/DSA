def kruskal(g):
    edges = []
    for v in g:
        for n, w in g[v]:
            edges.append((w, v, n))

    edges.sort()

    parent = {v: v for v in g}
    mst = []

    def find(v):
        if v != parent[v]:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        r1, r2 = find(v1), find(v2)
        parent[r1] = r2

    for w, sv, ev in edges:
        if find(sv) != find(ev):
            mst.append((sv, ev, w))
            union(sv, ev)

    return mst

# Function to initialize the graph with user input
def init_graph():
    g = {}
    m = int(input("Enter the number of edges: "))

    for _ in range(m):
        edge_info = input("Enter edge info (start_vertex end_vertex weight), separated by space: ").split()
        sv, ev, w = edge_info

        if sv not in g:
            g[sv] = []
        if ev not in g:
            g[ev] = []

        g[sv].append((ev, int(w)))
        g[ev].append((sv, int(w)))

    return g

# Main program
graph = init_graph()

# Run Kruskal's algorithm
mst_edges = kruskal(graph)

# Display the result
print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(edge)

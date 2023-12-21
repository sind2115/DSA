import heapq

def prim(g):
    s = input("Enter the starting vertex for Prim's algorithm: ")

    visited = set()
    pq = [(0, s, None)]
    mst = []

    while pq:
        w, cv, pv = heapq.heappop(pq)

        if cv not in visited:
            visited.add(cv)
            if pv is not None:
                mst.append((pv, cv, w))

            for n, ew in g[cv]:
                heapq.heappush(pq, (ew, n, cv))

    return mst

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

graph = init_graph()

mst_edges = prim(graph)

print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(edge)

import heapq
def dijkstra(g, s):
    d = {v: float('inf') for v in g}
    d[s] = 0
    pq = [(0, s)]
    while pq:
        cd, cv = heapq.heappop(pq)
        if cd > d[cv]:
            continue
        for n, w in g[cv]:
            dist = cd + w
            if dist < d[n]:
                d[n] = dist
                heapq.heappush(pq, (dist, n))
    return d
g = {}
e = int(input("Enter the number of edges: "))
for _ in range(e):
    edge_info = input("Enter edge information (start_vertex end_vertex weight), separated by space: ").split()
    sv, ev, w = edge_info
    w = int(w)
    if sv not in g:
        g[sv] = []
    if ev not in g:
        g[ev] = []
    g[sv].append((ev, w))
    g[ev].append((sv, w))
sv = input("Enter the start vertex: ")
dists = dijkstra(g, sv)
print(f"Shortest distances from {sv}: {dists}")

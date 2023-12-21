class Graph:
    def __init__(self, v):
        self.v = v
        self.e = []
    def add_edge(self, s, t, w):
        self.e.append((s, t, w))
    def dy_prg(self, s):
        dist = {vertex: float('infinity') for vertex in range(1, self.v + 1)}
        dist[s] = 0
        for _ in range(self.v - 1):
            for u, v, w in self.e:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.e:
            if dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle. Dynamic Programming  not applicable.")
                return
        return dist
def init_graph():
    v = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))
    g = Graph(v)
    for _ in range(e):
        edge_info = input("Enter edge information (start_vertex end_vertex weight), separated by space: ").split()
        s, t, w = map(int, edge_info)
        g.add_edge(s, t, w)
    return g
user_graph = init_graph()
source_vertex = int(input("Enter the source vertex: "))
shortest_distances = user_graph.dy_prg(source_vertex)
print("Shortest distances from the source vertex:")
for v, d in shortest_distances.items():
    print(f"To vertex {v}: {d}")

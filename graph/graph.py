class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adjacency_list = [[] for _ in range(V)]

    
    # Undirected graph
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

        self.E += 1

    def get_adjacency_list(self):
        return self.adjacency_list

graph = Graph(4)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print("V:", graph.V)
print("E:", graph.E)
print("Adjacency List:", graph.get_adjacency_list())
class CountPaths:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def count_from(self, node):
        if node in self.result:
            return self.result[node]

        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)

        self.result[node] = path_count
        return path_count

    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)


def create_edges():
    result = []
    for i in range(1, 100):
        result.append((i, i + 1))
        if i + 1 != 100:
            result.append((i, 100))
    result.append((1,99))
    print(result)
    return result

if __name__ == "__main__":
    edges = create_edges()

    counter = CountPaths(range(1, 100 + 1))
    for edge in edges:
        counter.add_edge(edge[0], edge[1])
    print(counter.count_paths(1, 100)) # 100
    
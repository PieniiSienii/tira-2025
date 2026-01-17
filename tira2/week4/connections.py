class Connections:
    def __init__(self, n):
        self.nodes = [i for i in range(1, n+1)]
        self.graph = {node: [] for node in self.nodes}
        self.reverse = {node: [] for node in self.nodes}

    def add_link(self, a, b):
        self.graph[a].append(b)
        self.reverse[b].append(a)

    def visit(self, node, phase):
        if node in self.visited:
            return
        self.visited.add(node)

        if phase == 1:
            graph = self.graph
        else:
            graph = self.reverse

        for next_node in graph[node]:
            self.visit(next_node, phase)
        
        if phase == 1:
            self.order.append(node)

    def check_network(self):
        self.visited = set()
        self.order = []

        for node in self.nodes:
            self.visit(node, 1)

        self.order.reverse()
        self.visited.clear()

        counter = 0
        for node in self.order:
            if node not in self.visited:
                counter += 1
                if counter > 1:
                    return False
                self.visit(node, 2)
        return True

if __name__ == "__main__":
    connections = Connections(5)

    connections.add_link(1, 2)
    connections.add_link(2, 3)
    connections.add_link(1, 3)
    connections.add_link(4, 5)

    print(connections.check_network()) # False

    connections.add_link(3, 5)
    connections.add_link(1, 4)

    print(connections.check_network()) # False

    connections.add_link(5, 1)

    print(connections.check_network()) # True
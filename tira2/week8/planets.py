class Planets:
    def __init__(self, n):
        self.n = n
        self.nodes = list(range(1, n + 1))
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_teleport(self, a, b):
        self.graph[(a, b)] += 1

    def min_removals(self):
        flow = self.graph.copy()
        total = 0

        def add_flow(node, sink, f):
            if node in seen:
                return 0
            seen.add(node)

            if node == sink:
                return f

            for nxt in self.nodes:
                if flow[(node, nxt)] > 0:
                    inc = add_flow(nxt, sink, min(f, flow[(node, nxt)]))
                    if inc > 0:
                        flow[(node, nxt)] -= inc
                        flow[(nxt, node)] += inc
                        return inc
            return 0

        while True:
            seen = set()
            inc = add_flow(1, self.n, float("inf"))
            if inc == 0:
                break
            total += inc

        return total


if __name__ == "__main__":
    planets = Planets(5)

    print(planets.min_removals())  # 0

    planets.add_teleport(1, 2)
    planets.add_teleport(2, 5)
    print(planets.min_removals())  # 1

    planets.add_teleport(1, 5)
    print(planets.min_removals())  # 2
    
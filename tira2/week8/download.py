class Download:
    def __init__(self, n):
        self.n = n
        self.nodes = list(range(1, n + 1))
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_link(self, a, b, x):
        self.graph[(a, b)] += x

    def max_data(self, a, b):
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
                    new_f = min(f, flow[(node, nxt)])
                    inc = add_flow(nxt, sink, new_f)
                    if inc > 0:
                        flow[(node, nxt)] -= inc
                        flow[(nxt, node)] += inc
                        return inc
            return 0

        while True:
            seen = set()
            inc = add_flow(a, b, float("inf"))
            if inc == 0:
                break
            total += inc

        return total


if __name__ == "__main__":
    download = Download(4)

    print(download.max_data(1, 4))  # 0

    download.add_link(1, 2, 5)
    download.add_link(2, 4, 6)
    download.add_link(1, 4, 2)
    print(download.max_data(1, 4))  # 7

    download.add_link(1, 3, 4)
    download.add_link(3, 2, 2)
    print(download.max_data(1, 4))  # 8

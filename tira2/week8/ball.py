class Ball:
    def __init__(self, n):
        self.n = n
        self.source = 0
        self.sink = 2 * n + 1
        self.nodes = list(range(self.sink + 1))

        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

        for i in range(1, n + 1):
            self.graph[(self.source, i)] = 1

        for i in range(1, n + 1):
            self.graph[(n + i, self.sink)] = 1

    def add_pair(self, a, b):
        self.graph[(a, self.n + b)] = 1

    def max_pairs(self):
        flow = self.graph.copy()
        total = 0

        def add_flow(node, f):
            if node in seen:
                return 0
            seen.add(node)

            if node == self.sink:
                return f

            for nxt in self.nodes:
                if flow[(node, nxt)] > 0:
                    inc = add_flow(nxt, min(f, flow[(node, nxt)]))
                    if inc > 0:
                        flow[(node, nxt)] -= inc
                        flow[(nxt, node)] += inc
                        return inc
            return 0

        while True:
            seen = set()
            inc = add_flow(self.source, float("inf"))
            if inc == 0:
                break
            total += inc

        return total


if __name__ == "__main__":
    ball = Ball(4)

    print(ball.max_pairs())  # 0

    ball.add_pair(1, 2)
    print(ball.max_pairs())  # 1

    ball.add_pair(1, 3)
    ball.add_pair(3, 2)
    print(ball.max_pairs())  # 2

    ball.add_pair(2, 1)
    print(ball.max_pairs())  # 3

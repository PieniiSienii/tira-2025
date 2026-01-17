# components.py

class Components:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def add_road(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        if self.size[a] < self.size[b]:
            a, b = b, a

        self.parent[b] = a
        self.size[a] += self.size[b]
        self.components -= 1

    def count(self):
        return self.components


if __name__ == "__main__":
    components = Components(5)

    print(components.count())  # 5

    components.add_road(1, 2)
    components.add_road(1, 3)
    print(components.count())  # 3

    components.add_road(2, 3)
    print(components.count())  # 3

    components.add_road(4, 5)
    print(components.count())  # 2

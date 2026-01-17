class NewRoads:
    def __init__(self, n):
        self.n = n
        self.roads = []

    def add_road(self, a, b, x):
        self.roads.append((x, a, b))

    def min_cost(self):
        parent = list(range(self.n + 1))
        size = [1] * (self.n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            return True

        self.roads.sort()
        total_cost = 0
        edges_used = 0

        for x, a, b in self.roads:
            if union(a, b):
                total_cost += x
                edges_used += 1
                if edges_used == self.n - 1:
                    return total_cost

        return -1


if __name__ == "__main__":
    new_roads = NewRoads(4)

    new_roads.add_road(1, 2, 2)
    new_roads.add_road(1, 3, 5)
    print(new_roads.min_cost())  # -1

    new_roads.add_road(3, 4, 4)
    print(new_roads.min_cost())  # 11

    new_roads.add_road(2, 3, 1)
    print(new_roads.min_cost())  # 7

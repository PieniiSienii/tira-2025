def connected(nodes, edges):
    if edges == [] and len(nodes) != 1:
        return False
    if len(edges) == 1:
        if sorted(edges[0]) != sorted(nodes):
            return False
    first = True
    neighbours = set()
    for edge in edges:
        if first:
            neighbours.add(edge[0])
            neighbours.add(edge[1])
            first = False
        if edge[0] not in neighbours and edge[1] not in neighbours:
            return False
        neighbours.add(edge[0])
        neighbours.add(edge[1])
    return True


if __name__ == "__main__":

    nodes = [1, 2, 3, 4]
    edges = [(1, 3), (2, 4), (3, 4), (1, 4)]
    print(connected(nodes, edges)) # True
    nodes = [1, 2, 3]
    edges = [(2, 3)]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges)) # True

    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(nodes, edges)) # True
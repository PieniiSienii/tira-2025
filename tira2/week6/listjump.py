import heapq

def find_steps(numbers):
    n = len(numbers)

    graph = {i: [] for i in range(n)}
    for i, step in enumerate(numbers):
        for j in [i + step, i - step]:
            if 0 <= j < n:
                graph[i].append((j, step))

    inf = float("inf")
    dist = [inf] * n
    dist[0] = 0
    queue = [(0, 0)]
    visited = set()

    while queue:
        cost, a = heapq.heappop(queue)
        if a in visited:
            continue
        visited.add(a)

        for b, c in graph[a]:
            new_cost = cost + c
            if new_cost < dist[b]:
                dist[b] = new_cost
                heapq.heappush(queue, (new_cost, b))
    return dist[-1] if dist[-1] != inf else -1


if __name__ == "__main__":
    print(find_steps([1, 1, 1, 1])) # 3
    print(find_steps([3, 2, 1])) # -1
    print(find_steps([3, 5, 2, 2, 2, 3, 5])) # 10
    print(find_steps([7, 5, 3, 1, 4, 2, 4, 6, 1])) # 32

    numbers = []
    for i in range(10**5):
        numbers.append(1337 * i % 100 + 1)
    print(find_steps(numbers)) # 100055
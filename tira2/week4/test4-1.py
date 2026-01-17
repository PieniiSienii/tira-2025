import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.max_depth += 1
            return

        depth = 0
        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    depth += 1
                    if depth > self.max_depth:
                        self.max_depth += 1
                    return
                depth += 1
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    depth += 1
                    if depth > self.max_depth:
                        self.max_depth += 1
                    return
                depth += 1
                node = node.right

    def height(self):
        return self.max_depth

if __name__ == "__main__":
    n = 1000
    n = 1000
    print("n:", n)
    random.seed(1337)
    numbers = [random.randint(1, 1000) for _ in range(n)]
    numbers_sorted = list(range(1,1001))
    test = TreeSet()
    for i in numbers:
        test.add(i)
    print(test.height())

    hihhuli = TreeSet()
    for i in numbers_sorted:
        hihhuli.add(i)
    print(hihhuli.height())
from collections import deque

class FlipList:
    def __init__(self):
        self.data = deque()
        self.rev = False

    def __repr__(self):
        if not self.rev:
            return "[" + ", ".join(map(str, self.data)) + "]"
        else:
            return "[" + ", ".join(map(str, reversed(self.data))) + "]"

    def add_first(self, x):
        if not self.rev:
            self.data.appendleft(x)
        else:
            self.data.append(x)

    def add_last(self, x):
        if not self.rev:
            self.data.append(x)
        else:
            self.data.appendleft(x)

    def flip(self):
        self.rev = not self.rev


if __name__ == "__main__":
    numbers = FlipList()

    numbers.add_last(1)
    numbers.add_last(2)
    numbers.add_last(3)
    print(numbers)  # [1, 2, 3]

    numbers.add_first(4)
    print(numbers)  # [4, 1, 2, 3]

    numbers.flip()
    print(numbers)  # [3, 2, 1, 4]

    numbers.add_last(5)
    print(numbers)  # [3, 2, 1, 4, 5]

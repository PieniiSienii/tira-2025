class PermutationTracker:
    def __init__(self):
        self.stack = set()
        self.has_dup = False
        self.min_num = float("inf")
        self.max_num = float("-inf")

    def append(self, number):
        if number in self.stack:
            self.has_dup = True
        else:
            self.stack.add(number)
            self.min_num = min(self.min_num, number)
            self.max_num = max(self.max_num, number)

    def check(self):
        if self.has_dup:
            return False
        if self.min_num != 1:
            return False
        if self.max_num != len(self.stack):
            return False
        else:
            return True

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False
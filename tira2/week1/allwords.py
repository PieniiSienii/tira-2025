import itertools
def create_words(word):
    correct_orders = set()

    for order in itertools.permutations(word):
        if valid_order(order):
            correct_orders.add("".join(order))
    return sorted(list(correct_orders))

def valid_order(order):
    for i in range(len(order)-1):
        if order[i] == order[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(create_words("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab")) # ['aba']
    print(create_words("aaab")) # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky', 
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    print(len(create_words("aybabtu"))) # 660
    print(len(create_words("abcdefgh"))) # 40320
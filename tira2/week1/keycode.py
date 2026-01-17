import itertools

def find_codes(pattern):
    list_n = [1,2,3,4,5,6,7,8,9]
    numbers = [int(n) for n in pattern if n != "?"]
    result = []
    for n in numbers:
        list_n.remove(n)

    for repetition in itertools.product(list_n, repeat=pattern.count("?")):
        if len(repetition) > 1:
            if len(repetition) != len(set(repetition)):
                continue

        new_code = list(pattern)
        indexes = set()
        for i, num in enumerate(pattern):
            if num == "?":
                indexes.add(i)

        i_counter = 0
        for r in range(4):
            if r in indexes:
                new_code[r] = str(repetition[i_counter])
                i_counter += 1
        result.append("".join(new_code))
    return result


if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024
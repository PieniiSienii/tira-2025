def count_substrings(string):
    seen = set()
    for length in range(1, len(string) + 1):
        for n in range(len(string) - length + 1):
            sub = string[n:n+length]
            if sub not in seen:
                seen.add(sub)
    return len(seen)
if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    # print(count_substrings("saippuakauppias")) # 110
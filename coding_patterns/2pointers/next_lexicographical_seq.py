def next_lexicographical_sequence(s: str = "abcd") -> str:
    # borked
    s = [char for char in s]
    start_pos = 0
    for i in range(start_pos + 1, len(s)):
        if s[i] > s[start_pos]:
            start_pos = i
    if start_pos == 0:
        return sorted(s)

    for i in range(start_pos - 1, 0, -1):
        if s[i] < s[start_pos]:
            s[i], s[start_pos] = s[start_pos], s[i]
        return "".join(s)


if __name__ == "__main__":
    print(next_lexicographical_sequence())

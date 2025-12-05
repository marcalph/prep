def next_lexicographical_sequence(s: str = "abcd") -> str:
    # borked
    chars = list(s)
    start_pos = 0
    for i in range(start_pos + 1, len(chars)):
        if chars[i] > chars[start_pos]:
            start_pos = i
    if start_pos == 0:
        return "".join(sorted(chars))

    for i in range(start_pos - 1, 0, -1):
        if chars[i] < chars[start_pos]:
            chars[i], chars[start_pos] = chars[start_pos], chars[i]
        return "".join(chars)
    return "".join(chars)


if __name__ == "__main__":
    print(next_lexicographical_sequence())

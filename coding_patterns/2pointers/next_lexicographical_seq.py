def next_lexicographical_sequence(s: str = "abcd") -> str:
    chars = list(s)
    r = len(chars) - 1
    # find pivot
    pivot = 0
    # ugly while
    while r > 1:
        if chars[r - 1] >= chars[r]:
            r -= 1
        else:
            pivot = r - 1
            break
    if pivot == 0:
        return "".join(chars[::-1])
    # find rightmost successor to pivot
    r = len(chars) - 1
    while r > pivot:
        if chars[pivot] > chars[r]:
            r -= 1
        else:
            chars[pivot], chars[r] = chars[r], chars[pivot]
            break
    # return string w/ pivot and rightmost successor swapped + suffix sorted
    return "".join(chars[: pivot + 1] + sorted(chars[pivot + 1 :]))


if __name__ == "__main__":
    print(next_lexicographical_sequence())

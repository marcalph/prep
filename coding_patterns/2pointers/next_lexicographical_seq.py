def next_lexicographical_sequence(s: str = "abcd") -> str:
    s = list(s)
    r = len(s) - 1
    # find pivot
    pivot = 0
    while r > 1:
        if s[r - 1] >= s[r]:
            r -= 1
        else:
            pivot = r - 1
            break
    if pivot == 0:
        return "".join(s[::-1])
    # find rightmost successor to pivot
    r = len(s) - 1
    while r > pivot:
        if s[pivot] > s[r]:
            r -= 1
        else:
            s[pivot], s[r] = s[r], s[pivot]
            break
    # return string w/ pivot and rightmost successor swapped + suffix sorted
    return "".join(s[: pivot + 1] + sorted(s[pivot + 1 :]))


if __name__ == "__main__":
    print(next_lexicographical_sequence())

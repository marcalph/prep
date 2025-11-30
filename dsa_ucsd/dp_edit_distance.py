def edit_distance(first_string, second_string):
    table = [
        [float("inf") for _ in range(len(second_string) + 1)]
        for _ in range(len(first_string) + 1)
    ]
    table[0] = list(range(len(second_string) + 1))
    for i in range(len(table)):
        table[i][0] = i
    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            table[i][j] = min(
                1 + table[i - 1][j], 1 + table[i][j - 1], 1 + table[i - 1][j - 1]
            )
            if first_string[i - 1] == second_string[j - 1]:
                table[i][j] = min(table[i][j], table[i - 1][j - 1])
    # import pprint
    # pprint.pprint(table)
    return table[-1][-1]


def edit_distance_iter(a, b):
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                table[i][j] = max(i, j)
            else:
                table[i][j] = min(
                    table[i][j - 1] + 1,
                    table[i - 1][j] + 1,
                    table[i - 1][j - 1] + (a[i - 1] != b[j - 1]),
                )

    return table[len(a)][len(b)]


from functools import lru_cache


@lru_cache(maxsize=10000)
def edit_distance_rec(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)

    return min(
        edit_distance(a, b, i, j - 1) + 1,
        edit_distance(a, b, i - 1, j) + 1,
        edit_distance(a, b, i - 1, j - 1) + (a[i - 1] != b[j - 1]),
    )


if __name__ == "__main__":
    print(edit_distance(input(), input()))

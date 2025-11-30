def lcs3(first_sequence, second_sequence, third_sequence):
    table = [
        [[0] * (len(third_sequence) + 1) for j in range(len(second_sequence) + 1)]
        for i in range(len(first_sequence) + 1)
    ]

    for i in range(len(first_sequence) + 1):
        for j in range(len(second_sequence) + 1):
            for k in range(len(third_sequence) + 1):
                if i == 0 or j == 0 or k == 0:
                    pass
                else:
                    table[i][j][k] = max(
                        table[i][j - 1][k],
                        table[i - 1][j][k],
                        table[i][j][k - 1],
                        table[i - 1][j - 1][k - 1]
                        + (
                            first_sequence[i - 1]
                            == second_sequence[j - 1]
                            == third_sequence[k - 1]
                        ),
                    )
    return table[-1][-1][-1]


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))

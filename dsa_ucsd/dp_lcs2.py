def lcs2(first_sequence, second_sequence):
    table = [[0] * (len(second_sequence) + 1) for _ in range(len(first_sequence) + 1)]

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                pass
            else:
                table[i][j] = max(
                    table[i][j - 1] ,
                    table[i - 1][j],
                    table[i - 1][j - 1] + (a[i - 1] == b[j - 1])
                )
    return table[len(a)][len(b)]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
def calculator(n):
    table = [float("inf")] * (n + 1)
    table[1] = 0

    for k in range(2, n + 1):
        table[k] = 1 + table[k - 1]
        if k % 2 == 0:
            table[k] = min(table[k], 1 + table[k // 2])
        if k % 3 == 0:
            table[k] = min(table[k], 1 + table[k // 3])

    operations = []
    while n > 1:
        operations.append(n)
        if table[n] == 1 + table[n - 1]:
            n = n - 1
        elif n % 2 == 0 and table[n] == 1 + table[n // 2]:
            n = n // 2
        elif n % 3 == 0 and table[n] == 1 + table[n // 3]:
            n = n // 3

    return [1] + list(reversed(operations))


if __name__ == "__main__":
    n = int(input())
    sequence = calculator(n)
    print(len(sequence) - 1)
    print(*sequence)

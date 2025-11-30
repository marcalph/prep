# Compute the n-th Fibonacci number modulo m.
def naive_fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


# +-----------+-----------------------------+------------------+
# |   m       | Fibonacci Sequence Mod m    | Pisano Period π(m)|
# +-----------+-----------------------------+------------------+
# |   2       | 0, 1, 1, 0, 1, 1, 0, 1, ... |        3         |
# +-----------+-----------------------------+------------------+
# |   3       | 0, 1, 1, 2, 0, 2, 2, 1, ... |        8         |
# +-----------+-----------------------------+------------------+
# |   4       | 0, 1, 1, 2, 3, 1, 0, 1, ... |        6         |
# +-----------+-----------------------------+------------------+


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1
    return 0


def fibonacci_huge(n, m):
    pisano_period = pisanoPeriod(m)
    # Taking mod of N with
    # period length
    if pisano_period:
        n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))

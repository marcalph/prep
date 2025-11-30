# Compute the last digit of the sum of fibonacci F_0+F_1+...+F_n
def naive_fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current = 0, 1

    for _ in range(n + 1):
        previous, current = current, previous + current

    return current % 10


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


def fibonacci_sum(n):
    return (fibonacci_huge(n + 2, 10) - 1) % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum(n))

# compute the last digit of the sum of squares of fibonacci numbers
# intuition is SSfib  = F_n * F_{n+1}
def naive_fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fib(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current

def fib_sum(from_):
    return fib((from_+2)%60)-1

def fib_partial_sum(from_,  to):
    return fib_sum(to) - fib_sum(from_)

def fibonacci_sum_squares(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return (fib_partial_sum(n-2, n)*fib_partial_sum(n-3, n-1))%10




if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))

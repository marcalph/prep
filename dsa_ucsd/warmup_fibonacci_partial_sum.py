# Compute the last digit of the partial sum from m to n i.e. F_m+F_{m+1}+...+F_n
import sys
def naive_fibonacci_partial_sum(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m
         
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1
    return 0
 
def fibonacci_huge(n,m):
    pisano_period = pisanoPeriod(m)
    # Taking mod of N with 
    # period length
    if pisano_period:
        n = n % pisano_period
     
    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current \
        = current, (previous + current)%m
         
    return current

def fibonacci_partial_sum(from_, to):
    return ((fibonacci_huge(to+2, 10)-1)-((fibonacci_huge(from_+1, 10)-1)))%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
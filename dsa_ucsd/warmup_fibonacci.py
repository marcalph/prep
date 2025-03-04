# simple fibonacci sequence
def naive_fib(n):
    if n <= 1:
        return n
    return naive_fib(n - 1) + naive_fib(n - 2)


def fib(n):
    if n <=1:
        return n
    nminus1, nminus2 = 0, 1
    for i in range(n):
        nminus1, nminus2 = nminus2, nminus1 + nminus2
    return nminus1
    



if __name__ == '__main__':
    input_n = int(input())
    print(fib(input_n))

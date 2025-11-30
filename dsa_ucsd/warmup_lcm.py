# least common multiple
#
def gcd(a, b):
    if b == 0:
        return a
    remainder = a % b
    return gcd(b, remainder)


def naive_lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False


def lcm(a, b):
    return int(abs(a * b) / gcd(a, b))


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))

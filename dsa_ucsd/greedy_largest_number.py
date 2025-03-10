from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    maxlen = max([len(str(s)) for s in numbers])
    numbers.sort(key=lambda a: "".join(list(str(a))*maxlen)[:maxlen])
    return "".join(numbers)



def largest_number_solution(xs):
    for _ in xs:
        for i in range(len(xs) - 1):
            if xs[i] + xs[i + 1] < xs[i + 1] + xs[i]:
                xs[i], xs[i + 1] = xs[i + 1], xs[i]

    return int("".join(xs))
               
if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_solution(input_numbers))

from sys import stdin


def best(valuesperweight):
    value = 0
    pick = None
    for i, v in enumerate(valuesperweight):
        if value <= v:
            value = v
            pick = i
    return pick


def optimal_value(capacity, weights, values):
    value = 0.0
    # write your code here
    valuespw = [v / w for v, w in zip(values, weights)]
    while capacity > 0:
        greedy_pick = best(valuespw)
        amount = min(weights[greedy_pick], capacity)
        capacity -= amount
        value += amount * valuespw[greedy_pick]
        valuespw[greedy_pick] = 0
    return value


def optimal_value_fast(capacity, weights, values):
    value = 0.0
    # value per wieght
    vpw = sorted([(v / w, w) for v, w in zip(values, weights)])
    while capacity > 0 and len(vpw) > 0:
        price, wi = vpw.pop()
        amount = min(wi, capacity)
        value += amount * price
        capacity -= amount
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = optimal_value_fast(capacity, weights, values)
    print("{:.10f}".format(opt_value))

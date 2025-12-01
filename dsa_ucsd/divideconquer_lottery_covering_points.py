from collections import namedtuple
from sys import stdin

Event = namedtuple("Event", ["coordinate", "type", "index"])


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    count = [None] * len(points)

    events = []
    for i in range(len(starts)):
        events.append(Event(starts[i], "l", i))
        events.append(Event(ends[i], "r", i))
    for i in range(len(points)):
        events.append(Event(points[i], "p", i))

    events = sorted(events)
    number_of_segments = 0
    for e in events:
        if e.type == "l":
            number_of_segments += 1
        elif e.type == "r":
            number_of_segments -= 1
        elif e.type == "p":
            count[e.index] = number_of_segments
        else:
            assert False

    return count


from collections import namedtuple
from sys import stdin

Event = namedtuple("Event", ["coordinate", "type", "index"])


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    count = [None] * len(points)

    events = []
    for i in range(len(starts)):
        events.append(Event(starts[i], "l", i))
        events.append(Event(ends[i], "r", i))
    for i in range(len(points)):
        events.append(Event(points[i], "p", i))

    events = sorted(events)
    number_of_segments = 0
    for e in events:
        if e.type == "l":
            number_of_segments += 1
        elif e.type == "r":
            number_of_segments -= 1
        elif e.type == "p":
            count[e.index] = number_of_segments
        else:
            assert False

    return count


from bisect import bisect_left, bisect_right


def points_cover_bisect(starts, ends, points):
    starts, ends = sorted(starts), sorted(ends)

    count = [len(starts)] * len(points)
    for index, point in enumerate(points):
        count[index] -= bisect_left(ends, point)
        count[index] -= len(starts) - bisect_right(starts, point)

    return count


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2 : 2 * n + 2 : 2], data[3 : 2 * n + 2 : 2]
    input_points = data[2 * n + 2 :]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)

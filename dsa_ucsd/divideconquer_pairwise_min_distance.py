from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple("Point", "x y")


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared, distance_squared(p, q))

    return min_distance_squared


def merge(points):
    points.sort(key=lambda x: x[1])
    mind = float("inf")
    for i, p in enumerate(points):
        for j in range(i + 1, min(i + 8, len(points))):
            mind = min(mind, distance_squared(p, points[j]))

    return mind


def min_distance_squared(points):
    if len(points) <= 4:
        return min(distance_squared(p, q) for p, q in combinations(points, 2))
    points.sort(key=lambda p: p.x)
    mid_index = len(points) // 2
    mid_x = points[mid_index].x
    leftd = min_distance_squared(points[:mid_index])
    rightd = min_distance_squared(points[mid_index:])
    d = min(leftd, rightd)

    pointsmiddle = [p for p in points if (p.x - mid_x) ** 2 < d]
    middled = merge(pointsmiddle)
    return min(d, middled)


if __name__ == "__main__":
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(min_distance_squared(sorted(input_points)))))

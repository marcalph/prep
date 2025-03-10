from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points_naive(segments):
    points = []
    # write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points


def is_covered(segment, point):
    return segment.left <= point <= segment.right


def segments_cover_(segments):
    points = list()
    while len(segments) > 0:
        r = min([s.right for s in segments])
        points.append(r)
        segments = [s for s in segments
                    if not is_covered(s, r)]

    return points
    


def segments_cover(segments):
    points = list()
    segments = sorted(segments, key=lambda s: s.end)
    r = -1
    for segment in segments:
        if r < segment.start:
            r = segment.end
            points.append(r)

    return points
    

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = segments_cover(segments)
    print(len(points))
    print(*points)

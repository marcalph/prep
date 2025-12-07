from typing import List


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def merge_overlapping_intervals(intervals: List[Interval]) -> List[Interval]:
    # Write your code here
    intervals.sort(key=lambda x: (x.start, x.end))
    res = [intervals[0]]
    for next_ in intervals[1:]:
        current = res[-1]
        if next_.start > current.end:
            res.append(next_)
        else:
            res[-1] = Interval(min(current.start, next_.start), max(current.end, next_.end))

    return res

from dataclasses import dataclass
from typing import List


@dataclass
class Word:
    text: str
    freq: int

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.text < other.text
        return self.freq > other.freq


def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    # could be done with a min heap, excluding evrything but topk
    from collections import Counter

    cnt = Counter(strs)
    import heapq

    heap = [Word(t, f) for t, f in cnt.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap).text for _ in range(k)]

from typing import List
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def combine_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    # Write your code here
    import heapq
    heap = []
    for ll in lists:
        node=ll
        while node:
            if node.val:
                heapq.heappush(heap, node.val)
            node = node.next
    print(heap)
    res = ListNode()
    head = ListNode()
    current = head
    while heap:
        current.val = heapq.heappop(heap)
        current.next = ListNode()
        current = current.next
    return head
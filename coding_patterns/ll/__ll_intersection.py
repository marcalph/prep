class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode | None:
    # Write your code here
    ptra = head_A
    ptrb = head_B
    while ptra != ptrb:
        ptra = ptra.next if ptra else head_B
        ptrb = ptrb.next if ptrb else head_A
    return ptra

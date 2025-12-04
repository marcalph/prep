
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



def linked_list_midpoint(head: ListNode) -> ListNode:
    # Write your code here
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
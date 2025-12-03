
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def linked_list_reversal(head: ListNode) -> ListNode:
    # Write your code here 
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current=next

        
    return prev
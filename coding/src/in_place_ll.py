from coding.src.ll import LinkedList
from coding.src.ll_node import LinkedListNode
            
def reverse(head):
    prev, current, next = None, head, None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    
    return head


def reverse_between(head, left, right):
    if not head or left == right:
        return head
    dummy = LinkedListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left-1):
        prev = prev.next
    current = prev.next

    for _ in range(right-left):
        next = current.next
        current.next = next.next
        next.next = prev.next
        prev.next = next


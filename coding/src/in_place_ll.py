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


def reverse_linked_list(head, k):
	previous, current, next = None, head, None
	for _ in range(k):
		next = current.next
		current.next = previous
		previous = current
		current = next
	return previous, current




def reverse_k_groups(head, k):
    dummy = LinkedListNode(0)
    dummy.next = head
    ptr = dummy

    while ptr:    
        tracker = ptr
        for i in range(k):
            if tracker == None:
                break
            tracker = tracker.next

        if tracker == None:
            break

        previous, current = reverse_linked_list(ptr.next, k)

        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group

    return dummy.next
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


def reverse_between(head: LinkedListNode | None, left: int, right: int) -> LinkedListNode | None:
    if not head or left == right:
        return head
    dummy: LinkedListNode = LinkedListNode(0)
    dummy.next = head
    prev: LinkedListNode = dummy

    for _ in range(left - 1):
        prev = prev.next  # type: ignore[assignment]
    current: LinkedListNode | None = prev.next

    for _ in range(right - left):
        next_node = current.next  # type: ignore[union-attr]
        current.next = next_node.next  # type: ignore[union-attr]
        next_node.next = prev.next  # type: ignore[union-attr]
        prev.next = next_node


def reverse_linked_list(head, k):
    previous, current, next = None, head, None
    for _ in range(k):
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous, current


def reverse_k_groups(head: LinkedListNode | None, k: int) -> LinkedListNode | None:
    dummy: LinkedListNode = LinkedListNode(0)
    dummy.next = head
    ptr: LinkedListNode | None = dummy

    while ptr:
        tracker: LinkedListNode | None = ptr
        for i in range(k):
            if tracker is None:
                break
            tracker = tracker.next

        if tracker is None:
            break

        previous, current = reverse_linked_list(ptr.next, k)

        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current  # type: ignore[union-attr]
        ptr.next = previous
        ptr = last_node_of_reversed_group

    return dummy.next

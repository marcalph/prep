class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def palindromic_linked_list(head: ListNode) -> bool:
    # Write your code here
    revll = linked_list_reversal(head)
    current = head
    revcurrent = revll
    while current:
        if current.val != revcurrent.val:
            return False
        current = current.next
        revcurrent = revcurrent.next
    return True


def linked_list_reversal(head: ListNode) -> ListNode:
    # Write your code here
    prev = None
    current = head
    while current is not None:
        node = ListNode(current.val)
        node.next = prev
        prev = node
        current = current.next

    return prev

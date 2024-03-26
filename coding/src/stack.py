"""
A Stack is suitable when you want to retrieve elements in the reverse order of their insertion (Last-In-First-Out or LIFO).

However, a Stack is not suitable when:

1. The problem requires retrieving elements in the same order as their insertion (First-In-First-Out or FIFO).
2. The order of outputs or processing operations is not significant.
"""


class Stack(list):
    def __init__(self, data: list[int]):
        super().__init__(data)

    def push(self, value):
        self.append(value)

    def pop(self):
        return super().pop()

    def peek(self):
        return self[-1]

    def is_empty(self):
        return len(self) == 0


def remove_duplicate_pairs(string):
    pseudo_stack = [string[0]]
    for char in string[1:]:
        if len(pseudo_stack) != 0 and char == pseudo_stack[-1]:
            pseudo_stack.pop()
        else:
            pseudo_stack.append(char)
    return "".join(pseudo_stack)

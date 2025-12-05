"""
A Stack is suitable when you want to retrieve elements in the reverse order of their insertion (Last-In-First-Out or LIFO).

However, a Stack is not suitable when:

1. The problem requires retrieving elements in the same order as their insertion (First-In-First-Out or FIFO).
2. The order of outputs or processing operations is not significant.
"""


class Stack(list):
    def __init__(self, data: list[int] | None = None):
        super().__init__(data or [])

    def push(self, value):
        self.append(value)

    def pop(self, index: int = -1):  # type: ignore[override]
        return super().pop(index)

    def peek(self):
        return self[-1]

    def is_empty(self):
        return len(self) == 0

    def size(self):
        return len(self)


def remove_duplicate_pairs(string):
    pseudo_stack = [string[0]]
    for char in string[1:]:
        if len(pseudo_stack) != 0 and char == pseudo_stack[-1]:
            pseudo_stack.pop()
        else:
            pseudo_stack.append(char)
    return "".join(pseudo_stack)


class MyQueue(object):
    def __init__(self):
        # Write your code here
        self._stack1 = Stack()
        self._stack2 = Stack()
        self._front = None

    def push(self, x):
        # Write your code here
        if self._stack1.is_empty():
            self._front = x
        self._stack1.push(x)

    def pop(self):
        # Write your code here
        while not self._stack1.is_empty():
            self._stack2.push(self._stack1.pop())
        result = self._stack2.pop()
        self._front = self._stack2.peek()
        while not self._stack2.is_empty():
            self._stack1.push(self._stack2.pop())
        return result

    def peek(self):
        # Write your code here
        return self._front

    def empty(self):
        # Write your code here
        return self._stack1.is_empty()


def calculator(s):
    s = s.replace(" ", "")
    print(s)
    sign, number, result = +1, "0", 0
    stack = []
    for char in s:
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            number += char
        elif char in ["-", "+"]:
            result += sign * int(number)
            number = "0"
            sign = [-1, 1][char == "+"]
        elif char in ["("]:
            stack.append((sign, result))
            number = "0"
            result = 0
            sign = 1
        else:
            result += sign * int(number)
            prev_sign, prev = stack.pop()
            result *= prev_sign
            result += prev
            number = 0

    return result + sign * int(number)

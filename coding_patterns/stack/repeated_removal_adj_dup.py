def repeated_removal_of_adjacent_duplicates(s: str) -> str:
    # Write your code here
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

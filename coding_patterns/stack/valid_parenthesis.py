def valid_parenthesis_expression(s: str) -> bool:
    stack = []

    for char in s:
        match char:
            case "(" | "[" | "{":
                stack.append(char)
            case ")":
                if not stack or stack.pop() != "(":
                    return False
            case "]":
                if not stack or stack.pop() != "[":
                    return False
            case "}":
                if not stack or stack.pop() != "{":
                    return False

    return len(stack) == 0

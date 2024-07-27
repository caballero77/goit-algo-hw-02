def is_brackets_correct(s):
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if len(stack) == 0:
                return False
            if c == ')' and stack[-1] == '(' or c == ']' and stack[-1] == '[' or c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return len(stack) == 0
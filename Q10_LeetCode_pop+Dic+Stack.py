def symbol(string):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []
    for s in string:
        if s in pairs:
            stack.append(s)
        else:
            if s != pairs[stack[-1]]:
                return False
            else:
                stack.pop()
    return len(stack) == 0


print(symbol("({]})"))

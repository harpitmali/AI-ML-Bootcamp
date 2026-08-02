def is_valid(s):
    stack = []

    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs.keys():
            if not stack:
                return False
            
            if stack[-1] != pairs[ch]:
                return False
            
            stack.pop()

    return len(stack) == 0

s = "([)]"

print(is_valid(s))
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int):
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value, self.min_stack[-1]))


    def pop(self) -> None:
        if not self.stack:
            return None

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def get_min(self) -> int:
        if not self.stack:
            return None
        return self.min_stack[-1]
    
stack = MinStack()

stack.push(5)
stack.push(3)
stack.push(8)
stack.push(1)

print(stack.get_min())   # 1

stack.pop()

print(stack.get_min())   # 3

print(stack.top())      # 8
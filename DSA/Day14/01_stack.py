"""def check_empty(stack):
    if not stack:
        print("Empty Stack")
    else:
        print("Not Empty Stack")

stack = []

check_empty(stack)

stack.append(10)
stack.append(20)
stack.append(30)

print(stack[-1])

stack.pop()

print(stack[-1])

check_empty(stack)"""

# Experiment 1

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print("Stack is Empty!")
            return
        else:
            return self.items.pop()

    def peek(self):
        if not self.items:
            print("Stack is Empty!")
            return
        else:
            return self.items[-1]

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())

print(stack.pop())

print(stack.peek())

print(stack.size())

print(stack.is_empty())
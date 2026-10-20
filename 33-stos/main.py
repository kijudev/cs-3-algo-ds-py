class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def peek(self):
        if len(self.data) == 0: return None
        return self.data[-1]

    def push(self, item):
        self.data.append(item)

    def pop(self):
        item = self.peek()
        self.data.pop()

        return item

    def __repr__(self):
        return f"Stack( data: {self.data} )"

stack = Stack()
print(stack)

stack.push(10)
print(stack)

stack.push(20)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

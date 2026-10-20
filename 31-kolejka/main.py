# @author Jakub Kijek
# @date 2026.10.20

class Queue:
    def __init__(self, capacity=4):
        self.data = [None] * capacity
        self.head = 0
        self.count = 0

    def size(self):
        return self.count

    def peek(self):
        if self.count == 0: return None
        return self.data[self.head]

    def enqueue(self, item):
        if self.count == len(self.data):
            self.data = [self.data[(self.head + i) % self.count] for i in range(self.count)] \
                        + [None] * self.count
            self.head = 0

        self.data[(self.head + self.count) % len(self.data)] = item
        self.count += 1

    def dequeue(self):
        if self.count == 0: return None

        item = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        self.count -= 1

        return item

    def __repr__(self):
        return f"Queue( head: {self.head}, count: {self.count}, data: {self.data} )"

queue = Queue()
print(queue)

for i in range(3): queue.enqueue(i)
print(queue)

queue.enqueue(20)
queue.enqueue(30)
print(queue)

queue = Queue(capacity=2)
print(queue)

queue.enqueue(0)
print(queue)

for i in range(1, 8): queue.enqueue(i)
print(queue)

queue = Queue(capacity=3)
print(queue)

for i in range(3): queue.enqueue(i)
print(queue)

queue.dequeue()
queue.enqueue(3)        
queue.enqueue(4)        
print(queue)


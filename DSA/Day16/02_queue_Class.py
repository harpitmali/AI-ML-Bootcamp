class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        return self.queue[0]
    
    def is_empty(self):
        return not self.queue
        
    def size(self):
        return len(self.queue)
    
q1 = Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

print(q1.front())

q1.dequeue()

print(q1.front())

print(q1.is_empty())
print(q1.size())
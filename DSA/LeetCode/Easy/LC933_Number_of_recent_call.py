from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)

        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)
    

counter = RecentCounter()

print(counter.ping(1))      # 1
print(counter.ping(100))    # 2
print(counter.ping(3001))   # 3
print(counter.ping(3002))   # 3
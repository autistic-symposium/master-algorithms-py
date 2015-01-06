class Queue():
    def __init__(self):
        self.in_ = []
        self.out = []

    def enqueue(self, item):
        self.in_.append(item)

    def deque(self):
        if not self.out:
            while self.in_:
                self.out.append(self.in_.pop())

        return self.out.pop()






q = Queue()
for i in range(10):
    q.enqueue(i)
for i in range(10):
    print(q.deque())
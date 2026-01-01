class HybridPriorityQueue():

    def init(self):
        self.Queue = []

    def insert(self,x, priority):
        for i in range(len(self.Queue)):
            if(self.Queue[i][1] > priority):
                self.Queue = self.Queue[:i] + [[x, priority]] + self.Queue[i:]
                return
        self.Queue.append((x, priority))
    def extract_max(self):
        if(len(self.Queue) == 0):
            return None
        last = self.Queue[-1]
        del self.Queue[-1]
        return last[0]

    def get_max(self):
        if(len(self.Queue) == 0):
            return None
        last = self.Queue[-1]
        return last[0]
    def remove(self,x):
        shouldRemove = []
        if(len(self.Queue) == 0):
            return None
        for i in range(len(self.Queue)):
            if(self.Queue[i][0] == x):
                shouldRemove.append(i)
        for i in shouldRemove:
            del self.Queue[i]                

    def change_priority(self,x, new_priority):
        for i in range(len(self.Queue)):
            if(self.Queue[i][0] == x):
                del self.Queue[i]
                self.insert(x, new_priority)
                return


hybrid_priority_queue = HybridPriorityQueue()

# Test case 1: Insert elements and get max
hybrid_priority_queue.insert(3, 2)
hybrid_priority_queue.insert(1, 5)
hybrid_priority_queue.insert(4, 3)
hybrid_priority_queue.insert(2, 4)
print(hybrid_priority_queue.get_max())  # Expected output: 1

# Test case 2: Extract max and get max
print(hybrid_priority_queue.extract_max())  # Expected output: 1
print(hybrid_priority_queue.get_max())  # Expected output: 2

# Test case 3: Change priority of an element and get max
hybrid_priority_queue.change_priority(4, 6)
print(hybrid_priority_queue.get_max())  # Expected output: 4

# Test case 4: Remove an element and get max
hybrid_priority_queue.remove(4)
print(hybrid_priority_queue.get_max())  # Expected output: 2

# Test case 5: Extract max until queue is empty
print(hybrid_priority_queue.extract_max())  # Expected output: 2
print(hybrid_priority_queue.extract_max())  # Expected output: 3
print(hybrid_priority_queue.get_max())  # Expected output: None
print(hybrid_priority_queue.extract_max())  # Expected output: None
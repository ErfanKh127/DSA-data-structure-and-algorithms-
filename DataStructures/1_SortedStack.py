class SortedStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def merge(self, left, right):
        merged = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged += left[left_index:]
        merged += right[right_index:]

        return merged

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)

    def get_sorted_elements(self):
        sorted_elements = self.merge_sort(self.items)
        return sorted_elements

sorted_stack = SortedStack()

# Test case 1: Add elements and get sorted elements
sorted_stack.push(3)
sorted_stack.push(1)
sorted_stack.push(4)
sorted_stack.push(2)
print(sorted_stack.get_sorted_elements())  # Expected output: [1, 2, 3, 4]

# Test case 2: Check top element
print(sorted_stack.top())  # Expected output: 2 (last pushed element)

# Test case 3: Pop element and get sorted elements
sorted_stack.pop()
print(sorted_stack.get_sorted_elements())  # Expected output: [1, 3, 4]

# Test case 4: Add more elements and get sorted elements
sorted_stack.push(5)
sorted_stack.push(0)
print(sorted_stack.get_sorted_elements())  # Expected output: [0, 1, 3, 4, 5]

# Test case 5: Pop all elements and check if stack is empty
sorted_stack.pop()
sorted_stack.pop()
sorted_stack.pop()
sorted_stack.pop()
sorted_stack.pop()
print(sorted_stack.get_sorted_elements())  # Expected output: []
print(sorted_stack.top())  # Expected output: None
print(sorted_stack.pop())  # Expected output: None

class DynamicSegmentArray:
    def __init__(self):
        self.capacity = 1
        self.segment_array = [0] * self.capacity
        self.size = 0

    def add(self, value):
        if self.size == self.capacity:
            self._double_capacity()
        self.segment_array[self.size] = value
        self.size += 1

    def _double_capacity(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.segment_array[i]
        self.segment_array = new_array

    def remove(self, value):
        if value in self.segment_array:
            self.segment_array.remove(value)
            self.size -= 1
            self.segment_array.append(0)

    def find(self, value):
        if value in self.segment_array:
            return self.segment_array.index(value)
        else:
            return -1

    def search_with_limit(self, value, k):
        new_array = [0] * (self.size+1)
        for i in range(self.size+1):
            new_array[i] = self.segment_array[i]
        for i in range(self.size+1):
            if k != 0:
                for j in range(i-k, i+k+1):
                    if new_array[j] == value:
                        break
                    elif j == i+k:
                        return -1
            else:
                if new_array[i] == value:
                    return i        
        return self.find(value)
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        left_idx = right_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1

        result.extend(left[left_idx:])
        result.extend(right[right_idx:])
        return result

    def range_query(self, l, r):
        if l < 0 or r >= len(self.segment_array) or l > r:
            raise ValueError("Index out of bounds")

        sub_array = self.segment_array[l:r+1]
        return self.merge_sort(sub_array)

dynamic_segment_array = DynamicSegmentArray()

# Test case 1: Add elements and find an element
dynamic_segment_array.add(3)
dynamic_segment_array.add(1)
dynamic_segment_array.add(4)
dynamic_segment_array.add(2)
dynamic_segment_array.add(3)
print(dynamic_segment_array.find(3))  # Expected output: 0

# Test case 2: Remove an element and find the element
dynamic_segment_array.remove(3)
print(dynamic_segment_array.find(3))  # Expected output: 3

# Test case 3: Add more elements and search with limit
dynamic_segment_array.add(5)
dynamic_segment_array.add(3)
print(dynamic_segment_array.search_with_limit(3, 2))  # Expected output: 3

# Test case 4: Remove an element that doesn't exist and check the array
dynamic_segment_array.remove(10)
print(dynamic_segment_array.find(10))  # Expected output: -1

# Test case 5: Search with limit and no element within limit
print(dynamic_segment_array.search_with_limit(4, 1))  # Expected output: -1

# Test case 6: Edge case with limit 0
print(dynamic_segment_array.search_with_limit(2, 0))  # Expected output: 3  >> correct is "2"

# Test case 7: Range query
dynamic_segment_array.add(10)
dynamic_segment_array.add(7)
print(dynamic_segment_array.range_query(1, 5))  # Expected output: [2, 3, 3, 4, 5]

# Test case 8: Range query with out of bounds
try:
    print(dynamic_segment_array.range_query(5, 10))
except Exception as e:
    print(e)  # Expected output: Index out of bounds
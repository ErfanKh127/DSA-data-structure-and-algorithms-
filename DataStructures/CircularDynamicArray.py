class CircularDynamicArray:

    
    def init(self):
        self.size = 0
        self.capacity = 2
        self.array = [0]*self.capacity

    def add(self,x):
        if(self.size == self.capacity):
            self.capacity *= 2
            newArray = [0]*self.capacity
            newArray[:self.size] = self.array
            self.array = newArray
            self.array[self.size] = x
            self.size += 1
        else:
            self.array[self.size] = x
            self.size += 1

    def remove(self,x):
        if(self.size == 0):
            return
        for i in range(self.size):
            if(self.array[i] == x):
                for j in range(i , self.size - 1):
                    self.array[j] = self.array[j+1]
                self.size -= 1
                break
        if(self.size < self.capacity // 4):
            self.capacity //= 2
            newArray = [0]*self.capacity
            for i in range(self.size):
                newArray[i] = self.array[i]
            self.array = newArray

    def find(self,x):
        if(self.size == 0):
            return
        for i in range(self.size):
            if(self.array[i] == x):
                return i
        return -1
    def get(self,index):
        if(self.size == 0):
            return
        if(index < 0 or index >= self.size):
            raise Exception("Index out of bounds")
        return self.array[index]
    def rotate(self,k):
        if(self.size == 0):
            return 
        else:
                for _ in range(k):
                    for i in range(self.size-1,0,-1):
                        if self.array[i]!=0:
                            last = self.array[i]
                            del self.array[i]
                            break
                    self.array = [last] + self.array  
    
    def reverse(self):
        first , last = 0 ,  self.size - 1
        if(self.size == 0):
            return
        else :
            while(first < last):
                self.array[first] , self.array[last] = self.array[last] , self.array[first]
                first += 1
                last -= 1
            

circular_dynamic_array = CircularDynamicArray()

# Test case 1: Add elements and get elements
circular_dynamic_array.add(1)
circular_dynamic_array.add(2)
circular_dynamic_array.add(3)
circular_dynamic_array.add(4)
circular_dynamic_array.add(5)
print([circular_dynamic_array.get(i) for i in range(5)])  # Expected output: [1, 2, 3, 4, 5]

# Test case 2: Find an element
print(circular_dynamic_array.find(3))  # Expected output: 2

# Test case 3: Remove an element and get elements
circular_dynamic_array.remove(3)
print([circular_dynamic_array.get(i) for i in range(4)])  # Expected output: [1, 2, 4, 5]

# Test case 4: Rotate the array and get elements
circular_dynamic_array.rotate(2)
print([circular_dynamic_array.get(i) for i in range(4)])  # Expected output: [4, 5, 1, 2]

# Test case 5: Reverse the array and get elements
circular_dynamic_array.reverse()
print([circular_dynamic_array.get(i) for i in range(4)])  # Expected output: [2, 1, 5, 4]

# Test case 6: Rotate the array back and get elements
circular_dynamic_array.rotate(2)
print([circular_dynamic_array.get(i) for i in range(4)])  # Expected output: [5, 4, 2, 1]

# Test case 7: Find an element that doesn't exist
print(circular_dynamic_array.find(10))  # Expected output: -1

# Test case 8: Get an element at an out of bounds index
try:
    print(circular_dynamic_array.get(10))
except Exception as e:
    print(e)  # Expected output: Index out of bounds
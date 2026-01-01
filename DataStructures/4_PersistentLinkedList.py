class Node:
    def init(self, value):
        self.value = value
        self.next = None

class version:
    def init(self,linkedList):
        self.Nodes = []
        self.head = linkedList.head
        headNode = linkedList.head
        while(headNode != None):
            self.Nodes.append(headNode)
            headNode = headNode.next

    def to_array(self):
        array = []
        for i in range(len(self.Nodes)):
            array.append(self.Nodes[i].value)
        return array
    
class PersistentLinkedList:
    def init(self):
        self.versions = []
        self.head = None

    def add(self,x):
        if(self.head == None):
            self.head = Node(x)
            self.head.next = None
            newVersion = version(self)
            self.versions.append(newVersion)
            return
        previousNode = self.head
        currentNode = Node(x)
        currentNode.next = None
        while(previousNode.next != None):
            previousNode = previousNode.next
        previousNode.next = currentNode
        newVersion = version(self)
        self.versions.append(newVersion)
    
    def remove(self,x):
        if(self.head == None):
            return "List is empty"
        if(self.head.value == x):
            self.head = self.head.next
            newVersion = version(self)
            self.versions.append(newVersion)
            return
        previousNode = self.head
        currentNode = self.head
        while(currentNode != None):
            if(currentNode.value == x):
                previousNode.next = currentNode.next
                newVersion = version(self)
                self.versions.append(newVersion)
                return
            previousNode = currentNode
            currentNode = currentNode.next
    
    def to_array(self):
        if(self.head == None):
            print("List is empty")
        array = []
        currentNode = self.head
        while(currentNode != None):
            array.append(currentNode.value)
            currentNode = currentNode.next
        return array
    
    def find(self,x):
        index = 0
        headNode = self.head
        while(headNode != None):
            if(headNode.value == x):
                return index
            headNode = headNode.next
            index += 1
        return -1
    
    def get_version(self,version) :
        for i in range(len(self.versions)):
            if(i == version-1):
                return self.versions[i]
        raise Exception("version not found")
    
    def rollback(self,version):
        for i in range(len(self.versions)):
            if(i == version-1):
                version = self.versions[i]
                self.head = version.head
                currentNode = self.head
                for i in range(1,len(version.Nodes),1):
                    currentNode.next = version.Nodes[i]
                    currentNode = currentNode.next
                return
                
        raise Exception("version not found")
    

persistent_list = PersistentLinkedList()

# Test case 1: Add elements and get version
persistent_list.add(3)  # version 1
persistent_list.add(1)  # version 2
persistent_list.add(4)  # version 3
version_3 = persistent_list.get_version(3)
print(version_3.to_array())  # Expected output: [3, 1, 4]

# Test case 2: Remove an element and get version
persistent_list.remove(1)  # version 4
version_4 = persistent_list.get_version(4)
print(version_4.to_array())  # Expected output: [3, 4]

# Test case 3: Rollback to a previous version and get current state
persistent_list.rollback(3)
print(persistent_list.to_array())  # Expected output: [3, 1, 4]

# Test case 4: Find an element in a rolled back version
print(persistent_list.find(4))  # Expected output: 2

# Test case 5: Add more elements after rollback and get version
persistent_list.add(5)  # version 5
persistent_list.add(2)  # version 6
version_6 = persistent_list.get_version(6)
print(version_6.to_array())  # Expected output: [3, 1, 4, 5, 2]
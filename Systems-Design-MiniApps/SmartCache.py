class SmartCache():

    def init(self) :
        self.cache = [[[None,0,None] for i in range(10)] for i in range(10)]

    def hash(self,key):
        i = (key * 2) % 10
        j = (key * 3) % 10
        
        return (i, j)

    def put(self,key, value):
        i, j = self.hash(key)
        self.cache[i][j][2] = key
        self.cache[i][j][0] = value

    def get(self,key):

        i, j = self.hash(key)
        self.cache[i][j][1] += 1
        return self.cache[i][j][0]
        

    def delete(self,key):   
        i,j = self.hash(key)
        if(self.cache[i][j][2] == key):
            self.cache[i][j][0] = None
        else:
            return None

    def evict(self):
        for i in range(10):
            for j in range(10):
                if(self.cache[i][j][0] != None):
                    if(self.cache[i][j][1] < 1):
                        self.cache[i][j][2] = None
                        self.cache[i][j][0] = None
                    

    def getAll(self):
        list = []
        for i in range(10):
            for j in range(10):
                if(self.cache[i][j][0] != None):
                    list.append(self.cache[i][j][0])
        return list



test = SmartCache()

test.put(1,"ali")   
test.put(12,"mahdi")
test.put(20,"mohammad")
test.put(45,"amir")

print(test.getAll())

print(test.delete(2))
print(test.delete(3))


print(test.getAll())

print(test.get(20))
print(test.get(45))

print(test.getAll())

test.evict()

print(test.getAll())
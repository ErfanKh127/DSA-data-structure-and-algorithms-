n = int(input())
list = list(map(int,input().split(' ')))
moves = 0

def isSorted():
    Sorted = True
    for i in range(n-1):
        if(list[i]>list[i+1]):
            Sorted = False
    return Sorted

def swap(x,y):
    temp = list[x]
    list[x] = list[y]
    list[y] = temp
    
def sortWithMinMove():
    global moves
    for i in range(n-1,-1,-1):
        for j in range(0,i,1):
            if(list[i]<list[j]):
                swap(i,j)
                print("Swap(" + str(list[i]) +"," + str(list[j])+") -->",end="")
                print(list)
                moves+=1
            if(isSorted()):
                return

sortWithMinMove()
print(moves)
        

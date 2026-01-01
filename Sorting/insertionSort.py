n = int(input())
A=list(input().split(" "))
step=0
def insertion():
    global step
    for k in range(1,len(A)):
        item = A[k]
        i=k
        while(i>0):
            if(A[i-1]>item):
                step+=1
            i-=1
    return step
print(insertion())
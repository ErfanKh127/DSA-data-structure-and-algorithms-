try:
    n , m = map(int,input().split(" "))
    list = list(map(int,input().split(" ")))
except:
    print(0)
    exit(0)

totalChance = 0

def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

def merge(left, right):
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

def range_query(l, r):
        sub_array = list[l:r+1]
        sub_array = merge_sort(sub_array)
        return sub_array

def calculate_mean(i):
     sub_arr = range_query(i-m, i)
     mean = 0.0
     mid = ((m+1)//2)
     if(m/2 == m//2):
          mean = (sub_arr[mid-1] + sub_arr[mid]) / 2
          return mean
     else:
          mean = sub_arr[mid-1]
          return mean

if(len(list) < n or m > n or (m < 1 or n < 1)):
    print(0)
    exit(0)

for i in range(m,n,1):
    mean = calculate_mean(i)
    if(list[i] >= (mean * 2)):
        totalChance += 1

print(totalChance)
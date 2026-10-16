import random

list = [random.randint(1,100) for i in range(10)]
print(list)

def merge(low, mid, high):
    templist = []
    start1 = low
    start2 = mid + 1
    while start1 <= mid and start2 <= high:
        if list[start1] > list[start2]:
            templist.append(list[start2])
            start2 += 1
        else:
            templist.append(list[start1])
            start1 += 1
    while start1 <= mid:
        templist.append(list[start1])
        start1 += 1
    while start2 <= high:
        templist.append(list[start2])
        start2 += 1
    j = 0
    for i in range(low, high + 1):
        list[i] = templist[j]
        j += 1
 
def mergesort(low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(low, mid)
        mergesort(mid+1, high)
        merge(low,mid,high)

mergesort(low=0, high=9)
print(list)
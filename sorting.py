#1

list = ["apple", "kiwi", "banana", "pie", "date"]
print(list)
for i in range(1, len(list)):
    j = i-1
    key = list[i]
    while j >= 0 and list[j] > key:
        list[j+1] = list[j]
        j-=1
    list[j+1] = key
    print(list)

#2
import random

list = [5,4,1,3,2]
print(list)
# list2 = [18, 1, 1, 5, 13, 4, 8, 12, 2, 9]
# list = [18, 1, 1, 5, 13, 4, 8, 12, 2, 9]
count = 0
c = 0
for i in range(len(list)):
    swapped = False
    for j in range(len(list) - i - 1):
        c += 1
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            count += 1
            swapped = True
        print(list)
    if swapped == False:
        print("swapped") 
        break   
print(list, count, c)
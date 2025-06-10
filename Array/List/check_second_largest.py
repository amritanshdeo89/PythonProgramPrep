arr = [10, 10, 10]
# [12, 35, 1, 10, 34, 1]
# [10, 5, 10]
# [10, 10, 10]

# sort array first --> 1st way
# arr.sort()
# print(f'Scond largest is : {arr[-2]}')

# assign -1 to largest and second_largest 

largest = -1
second_largest = -1 

for i in range(len(arr)):
    if arr[i] > largest:
       second_largest = largest
       largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]
    
print(second_largest)
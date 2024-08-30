def sumOfArray(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    return sum

print(f'Sum of given array is : {sumOfArray([10, 21, 12, 13])}')
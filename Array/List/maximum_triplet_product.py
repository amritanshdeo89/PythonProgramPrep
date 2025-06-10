arr = [-10, -3, -5, -6, -20]
# [10, 3, 5, 6, 20]
# [-10, -3, -5, -6, -20]
# [1, -4, 3, -6, 7, 0]

largest = second_largest = third_largest = float('-inf')

for i in range(len(arr)):
    if arr[i] > largest:
        third_largest = second_largest
        second_largest = largest
        largest = arr[i]

    elif arr[i] > second_largest and arr[i] != largest:
        third_largest = second_largest
        second_largest = arr[i]

    elif arr[i] > third_largest and arr[i] != second_largest:
        third_largest = arr[i]

triplet_product = (largest*second_largest*third_largest)

print(triplet_product)
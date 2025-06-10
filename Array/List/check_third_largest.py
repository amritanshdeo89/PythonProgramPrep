arr = [10, 10, 10, 9]
#[1, 14, 2, 16, 10, 20]
# [855, 450, 132, 359, 233, 825, 604, 481, 262, 337, 720, 525, 652, 300, 906, 219, 926, 906, 293, 864, 817, 498, 30, 639, 661]

largest = -1
second_largest = -1
third_largest = -1

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

print(third_largest)


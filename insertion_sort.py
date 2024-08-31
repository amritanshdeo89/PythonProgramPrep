def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]  # assigning first value as key
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j] # assigning 0 index value 1
            j -= 1            # decrement index value
        
        arr[j+1] = key        # assign key at after the element just smaller than it.
    
    return arr

arr = [12, 11, 13, 5, 6]

print(f"Sorted array is : {insertion_sort(arr)}")


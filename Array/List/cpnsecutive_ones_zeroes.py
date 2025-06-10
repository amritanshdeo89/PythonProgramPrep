arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]

count = 0
max_count = 0

for i in range(1,len(arr)):
    if arr[i-1] == arr[i]:
        count += 1
        max_count = max(count, max_count)
    else: 
         count = 0
   
   

print(max_count)
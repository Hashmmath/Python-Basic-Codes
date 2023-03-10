def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Get user input for the array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Sort the array using selection sort
sorted_arr = selection_sort(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)

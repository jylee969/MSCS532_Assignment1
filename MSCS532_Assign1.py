def insertion_sort_decreasing(arr):
    # Traverse through 1 to len(arr)
    # This loop starts from the second element because the first element is already sorted 
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are smaller than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
# data = [12, 11, 13, 5, 6]
# insertion_sort_decreasing(data)
# print("Sorted array in decreasing order:", data)

# Testing the function
if __name__ == "__main__":
    data = [15, 12, 18, 20, 8]
    print("Original array:", data)
    insertion_sort_decreasing(data)
    print("Sorted array in decreasing order:", data)
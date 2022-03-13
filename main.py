def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

sample_array = [ 2, 3, 4, 10, 40 ]
target_integer = int(input("target integer >>> "))

result = binary_search(sample_array, target_integer)
 
if result != -1:
    print("Element index: " + str(result))
else:
    print("404 not found.")
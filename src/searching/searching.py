# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, start, end, target):
    # Your code here
    # Check base case
    if start >= end:
        mid = (start + end) // 2
        # If elemnt is present at the middle itself
        if arr[mid] == target:
            return mid
        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > target:
            return binary_search(arr, end, mid -1, target)
        # Else the element can only be in the right subarray
        else:
            return binary_search(arr, mid + 1, start, target )
    else:
        # Target is not present in the array
        return -1
            

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

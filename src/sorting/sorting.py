# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    arrC = arrA + arrB
    for i in range(0, len(arrC) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i+1, len(arrC)):
            if arrC[j] < arrC[smallest_index]:
                smallest_index = j

        arrC[i], arrC[smallest_index] = arrC[smallest_index], arrC[i]

    return arrC

# TO-DO: implement the Merge Sort function below recursively
arr1 = [4,46,7,8,99,2,88,52,41,36,22]
arr2 = [3,5,76,98,12]

print(merge(arr1, arr2))

def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        mid = int(len(arr) / 2)
        arr1 = merge_sort(arr[0:mid])
        arr2 = merge_sort(arr[mid:])
        arr = merge(arr1, arr2)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

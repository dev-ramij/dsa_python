def BinarySearch(arr, first, last, k):
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == k:
            return mid
        if arr[mid] > k:
            last = mid - 1
        else:
            first = mid + 1
    return -1


def Search(arr, n, k):
    
    pivot = -1
    if n == 0:
        return -1
    if n == 1:
        if k == arr[0]:
            return 0
        else:
            return -1

    for i in range(n - 1):
        curr_idx = n - 1 - i
        if arr[curr_idx] == k:
            return curr_idx
        if curr_idx == 0:
            break
        if arr[curr_idx] < arr[curr_idx - 1]:
            pivot = curr_idx
            break
    if pivot == -1:
        return BinarySearch(arr, 0, n - 1, k)
    if k >= arr[0] and k <= arr[pivot - 1]:
        return BinarySearch(arr, 0, pivot - 1, k)
    if k >= arr[pivot] and k <= arr[n - 1]:
        return BinarySearch(arr, pivot, n - 1, k)
    return -1


print(Search([5, 6, 7, 8, 9, 10, 1, 2, 3], 9, 10))

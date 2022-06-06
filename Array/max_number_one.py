# Given a binary array arr of size N and an integer M.
# Find the maximum number of consecutive 1's produced by flipping at most M 0's.

def findZeroes(arr, n, m):
    max_length = 0
    left = 0
    zeros = []
    for i in range(n):
        # If find zero append it to the zeros array 
        if arr[i] == 0:
            zeros.append(i)
        # when zero exceeds the number then pop the first element and left will be the next 
        if len(zeros) > m:
            left = zeros.pop(0) + 1

        # check max_length and assigned if required
        if i - left + 1 > max_length:
            max_length = i - left + 1

    return max_length


print(findZeroes([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 11, 2))

# Given a sorted array Arr[](0-index based) consisting of N distinct integers and an integer k,
# the task is to find the index of k,if it’s present in the array Arr[].
# Otherwise, find the index where k must be inserted to keep the array sorted.


class Solution:

    def searchInsertK(self, Arr, N, k):
        if N == 0:
            return -1
        if N == 1:
            if k <= Arr[0]:
                return 0
            else:
                return 1
        if k <= Arr[0]:
            return 0
        elif k == Arr[N - 1]:
            return N - 1
        elif k > Arr[N - 1]:
            return N
        first = 0
        last = N - 1
        while first <= last:
            mid = (first + last) // 2
            if Arr[mid] == k:
                return mid
            if k > Arr[mid - 1] and k < Arr[mid]:
                return mid
            elif k < Arr[mid + 1] and k > Arr[mid]:
                return mid + 1
            if k > Arr[mid]:
                first = mid + 1
            else:
                last = mid - 1
        return -1


objects = Solution()
print(objects.searchInsertK([1, 3, 5, 6], 4, 7))

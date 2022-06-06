# Given an array of integers. Find the Inversion Count in the array.

# Inversion Count: For an array, inversion count indicates how far (or close)
# the array is from being sorted. If array is already sorted then the inversion count is 0.
# If an array is sorted in the reverse order then the inversion count is the maximum.
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.


class Solution:

    def inversionCount(self, arr, n):
        count = 0
        sorted_array = arr.copy()
        sorted_array.sort()
        for i in range(n):
            l = 0
            r = n - 1
            idx = -1
            while l <= r:
                mid = (l + r) // 2

                if sorted_array[mid] == arr[i]:
                    idx = mid
                    break
                if sorted_array[mid] < arr[i]:
                    l = mid + 1
                else:
                    r = mid - 1
            if idx > i:
                count += (idx - i)
        return count


ob = Solution()
print(ob.inversionCount([2, 4, 1, 3, 5], 5))


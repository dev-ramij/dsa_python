# Given an array arr[] of N positive integers.
# Find maximum value of |arr[i] – arr[j]| + |i – j|, (0 <= i, j <= N – 1)


class Solution:

    def maxValue(self, arr, N):
        max1 = arr[0]
        min1 = arr[0]
        max2 = arr[0]
        min2 = arr[0]

        for i in range(1, N):
            if arr[i] - i > max1:
                max1 = arr[i] - i
            if arr[i] - i < min1:
                min1 = arr[i] - i
            if arr[i] + i > max2:
                max2 = arr[i] + i
            if arr[i] + i < min2:
                min2 = arr[i] + i

        if max1 - min1 > max2 - min2:
            return max1 - min1
        else:
            return max2 - min2


objects = Solution()
print(
    objects.maxValue([
        34, 98, 13, 47, 21, 45, 99, 54, 82, 30, 3, 68, 62, 4, 31, 53, 51, 97,
        12, 23, 7, 27, 89, 67, 44, 11, 37, 40, 32, 46, 73, 55, 26, 5, 98, 89
    ], 36))

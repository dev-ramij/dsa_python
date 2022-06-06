# Given a sorted array arr[] of distinct integers.
# Sort the array into a wave-like array and return it
# In other words, arrange the elements into a sequence
# such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
# If there are multiple solutions, find the lexicographically smallest one.


class Solution:

    def convertToWave(self, arr, N):
        for i in range(N):
            if i == N - 1 and i % 2 !=1:
                break
            if i % 2 == 1:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]


ob = Solution()
print(ob.convertToWave([1, 2, 3, 4, 5], 5))

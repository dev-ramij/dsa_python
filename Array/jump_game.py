# Given an positive integer N and a list of N integers A[].
# Each element in the array denotes the maximum length of jump you can cover.
# Find out if you can make it to the last index if you start at the first index of the list.


class Solution:

    def canReach(self, A, N):
        if N == 0 or A[0] == 0:
            return 0
        if N == 1:
            return 1

        l = 0
        r = l + A[l]
        while l <= r:
            if r >= N - 1 or r + A[r] >= N - 1:
                return 1
            if l == r:
                return 0
            if A[r + A[r]] > 0 or A[l] < A[r]:
                l = r
                r = l + A[l]
            else:
                r -= 1
        return 0


obj = Solution()
print(obj.canReach([1, 0, 2], 3))

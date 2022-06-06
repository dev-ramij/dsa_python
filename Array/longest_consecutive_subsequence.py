# Given an array of positive integers.
# Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers,
# the consecutive numbers can be in any order.


class Solution:

    def findLongestConseqSubseq(self, arr, N):
        arr.sort()
        max_length = 1
        cont_length = 1
        if N == 0:
            return 0
        for i in range(1, N):
            if arr[i] == arr[i - 1]:
                continue
            if arr[i] == arr[i - 1] + 1:
                cont_length += 1
            else:
                if cont_length > max_length:
                    max_length = cont_length
                cont_length = 1
        if cont_length > max_length:
            max_length = cont_length
        return max_length


ob = Solution()
print(
    ob.findLongestConseqSubseq(
        [6, 6, 2, 3, 1, 4, 1, 5, 6, 2, 8, 7, 4, 2, 1, 3, 4, 5, 9, 6], 20))

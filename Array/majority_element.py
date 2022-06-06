# Given an array A of N elements. Find the majority element in the array.
# A majority element in an array A of size N is an element that appears more than N/2 times in the array.


class Solution:

    def majorityElement(self, A, N):
        hashmap = {}
        if N == 1:
            return A[0]
        for i in range(N):
            if A[i] in hashmap:
                hashmap[A[i]] += 1
                if hashmap[A[i]] > N // 2:
                    return A[i]
            else:
                hashmap[A[i]] = 1
        return -1


ob = Solution()
print(ob.majorityElement([3, 1, 3, 3, 2], 5))

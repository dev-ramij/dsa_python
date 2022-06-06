class Solution:

    #Function to find if there exists a triplet in the
    #array A[] which sums up to X.
    def find3Numbers(self, A, n, X):
        l = 0
        r = 1
        hashMap = {}

        while l < n:
            # assigned r to its right pointer
            r = l + 1
            while r < n:
                sum_of_two = A[l] + A[r]
                remaining = X - sum_of_two
                # check remaining is exist in hashmap with different index
                if remaining in hashMap and r != hashMap[remaining]:
                    return 1
                if A[r] not in hashMap:
                    hashMap[A[r]] = r
                r += 1
            l += 1
        return 0

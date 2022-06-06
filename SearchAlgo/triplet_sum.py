# Given an array Arr[] of N distinct integers and a range from L to R,
# the task is to count the number of triplets having a sum in the range [L, R].


class Solution:

    def countTriplets(self, Arr, N, L, R):
        Arr.sort()
        count1 = 0
        for i in range(N - 2):
            l = i + 1
            r = N - 1
            while l < r:
                sum = Arr[i] + Arr[l] + Arr[r]
                
                if sum > R:
                    r -= 1
                else:
                    count1 += (r - l)
                    l += 1
        count2 = 0
        for i in range(N - 2):
            l = i + 1
            r = N - 1
            while l < r:
                sum = Arr[i] + Arr[l] + Arr[r]
                if sum > L-1:
                    r -= 1
                else:
                    count2 += (r - l)
                    l += 1
        return count1 - count2


ob = Solution()
print(ob.countTriplets([9, 4, 6, 1, 2, 3, 8], 7, 3, 14))

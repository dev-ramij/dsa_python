# First init dp with length 1
# start from i = 1 and j = 0
# if get the jth value is lesser than ith value then update the length if dp[j]+1 is maximum
# return max of length
class Solution:

    def longestSubsequence(self, a, n):
        dp = [1]* n
        if n == 1:
            return 1
        i = 1
        j = 0
        while i < n:
            if i == j:
                j = 0
                i +=1
                continue
            if a[i] > a[j]:
                curr_max = dp[j]+1
                if dp[i] < curr_max:
                    dp[i] = curr_max
            j+=1 
        return max(dp)            
    

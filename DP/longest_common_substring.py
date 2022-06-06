
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = []
        # creating dp [n*m] matrix and assigned all value as zero
        for i in range(n):
            dp.append([])
            for j in range(m):
                dp[i].append(-1)
        # generating max_len matrix
        for i in range(n):
            for j in range(m):
                if S1[i] == S2[j]:
                    # if i or j is in 0 then there will not be any diagonal elements
                    # so assign it to 1 as max_len
                    if i == 0 or j ==0:
                        dp[i][j] = 1
                    # if diagonal present then length will be 1+dp[diagonal]
                    else:
                        dp[i][j] = 1+ dp[i-1][j-1]
                # if not equal assign 0
                else:
                    dp[i][j] = 0
        max_len = 0
        # getting the max_len
        for i in range(n):
            for j in range(m):
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
        return max_len



ob = Solution()
print(ob.longestCommonSubstr("adac","adadac",4,6))
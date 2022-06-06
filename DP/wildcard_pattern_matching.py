# We are appending an matix of n*m where all value is False
# Assign (0,0) as True for empty string
# If pattern is starting from * then need to assign True in that case 
# we will assign the left value to it
class Solution:
    def wildCard(self,pattern, string):
        len_p = len(pattern)
        len_s = len(string)
        dp =[]

        for i in range(len_s+1):
            dp.append([])
            for j in range(len_p+1):
                dp[i].append(False)
        dp[0][0] = True
        for j in range(1,len_p+1):
            if pattern[j-1] == "*":
                dp[0][j] = dp[0][j-1]
        for i in range(1,len_s+1):
            for j in range(1,len_p+1):
                if string[i-1] == pattern[j-1] or pattern[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[len_s][len_p]

ob = Solution()
print(ob.wildCard("*ceebce*","ceebce"))


# create a dp array for memoisation
# find all recursive call and update the lowest number
import sys
class Solution:
    def coinHelper(self,coins,M,V,dp):
        if V == 0:
            return 0
        ans = sys.maxsize
        for i in range(M):
            
            if V - coins[i] >= 0:
                if dp[V-coins[i]] != -1:
                    subAns = dp[V-coins[i]]
                else:
                    subAns = self.coinHelper(coins, M, V - coins[i],dp)
                if subAns != sys.maxsize and subAns + 1 < ans:
                    ans = subAns + 1
        dp[V] = ans
        return ans

    def minCoins(self, coins, M, V):
        dp = [-1] * (V+1)
        dp[0] = 0
        ans = self.coinHelper(coins,M,V,dp)
        if ans == sys.maxsize:
            return -1
        return ans
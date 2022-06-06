import sys


class Solution:
    maxV = sys.maxsize
    def maxHelper(self,n,x,y,z,dp):
        if n == 0:
            return 0
        ans = - self.maxV
        xcut = -self.maxV
        ycut = -self.maxV
        zcut = -self.maxV
        print(n-x,n-y,n-z)
        if n-x>=0:
            if dp[n-x] != -1:
                xcut = dp[n-x]
            else:
                xcut = self.maxHelper(n-x,x,y,z,dp)
        if n-y>=0:
            if dp[n-y] != -1:
                ycut = dp[n-y]
            else:
                ycut = self.maxHelper(n-y,x,y,z,dp)
        if n-z>=0:
            if dp[n-z] != -1:
                zcut = dp[n-z]
            else:
                zcut = self.maxHelper(n-z,x,y,z,dp)
        ans = max(xcut,ycut,zcut) +1
        dp[n] = ans
        return ans
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        
        dp = [-1] * 100004
        dp[0] = 0
        ans = self.maxHelper(n,x,y,z,dp)
        return ans

ob = Solution()
print(ob.maximizeTheCuts(4000,1,2,3))
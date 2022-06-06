class Solution:

    hashMap = {}

    def countWays(self, n):
        if n == 0:
            return 1
        count1 = 0
        count2 = 0
        if n >= 0:
            if n-1 in self.hashMap:
                count1 = self.hashMap[n-1]
            else:
                count1 = self.countWays(n - 1)
            if n-2 in self.hashMap:
                count2 = self.hashMap[n-2]
            else:
                count2 = self.countWays(n - 2)
        self.hashMap[n] = count1+count2
        return (count1 + count2) % (10**9+7)

ob = Solution()
print(ob.countWays(4))
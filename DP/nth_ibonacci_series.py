class Solution:
    dpHash = {}

    def nthFibonacci(self, n):
        if n <=2:
            return 1
        ans1 = 0
        ans2 = 0

        if n-1 in self.dpHash:
            ans1 = self.dpHash[n-1]
        else:
            ans1 = self.nthFibonacci(n - 1)
        if n-2 in self.dpHash:
            ans2 = self.dpHash[n-2]
        else:
            ans2 = self.nthFibonacci(n - 2)
        ans = ans1+ ans2
        self.dpHash[n] = ans
        return ans
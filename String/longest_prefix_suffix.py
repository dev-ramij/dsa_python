class Solution:
    def lps(self, s):
        n =len(s)
        
        for i in range(1,n):
            left_str = s[:n-i]
            right_str = s[i:]
            if left_str == right_str:
                return n-i
        return 0
ob = Solution()
print(ob.lps("abab"))
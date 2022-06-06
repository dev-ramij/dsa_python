
class Solution:

    def permutate(self, str, results, s, n):
        if len(str) == n:
            results.append(str)
        for i in range(len(s)):
            remaining_str = s[:i] + s[i + 1:]
            self.permutate(str + s[i], results, remaining_str, n)

    def permutation(self, s):
        results = []
        str = ""
        self.permutate(str, results, s, len(s))
        return results


ob = Solution()
print(ob.permutation("ABC"))
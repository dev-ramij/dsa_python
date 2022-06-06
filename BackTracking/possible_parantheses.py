class Solution:

    def createParantheses(self, str, n, countL, countR, bracket, results):
        if countL == n and countR == n and str[
                n * 2 - 1] != "(" and str not in results:
            results.append(str)
            return
        if countL > n or countR > n or countR > countL:
            return
        if bracket == "(":
            countL += 1
        else:
            countR += 1
        self.createParantheses(str + bracket, n, countL, countR, "(", results)
        self.createParantheses(str + bracket, n, countL, countR, ")", results)

    def AllParenthesis(self, n):
        str = ""
        results = []
        self.createParantheses(str, n, 0, 0, "(", results)
        return results


ob = Solution()
print(ob.AllParenthesis(3))
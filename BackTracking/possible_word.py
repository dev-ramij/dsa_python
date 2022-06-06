class Solution:

    def combineWord(self, str, N, results, stra, index):
        if len(str) == N:
            results.append("".join(str))
        else:
            current_str = stra[index]
            for i in range(len(current_str)):
                str.append(current_str[i])
                self.combineWord(str, N, results, stra, index + 1)
                str.pop()

    def possibleWords(self, a, N):
        numberMap = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
            0: ""
        }
        stra = []
        for i in range(N):
            stra.append(numberMap[a[i]])
        results = []
        strArr = []

        self.combineWord(strArr, N, results, stra, 0)
        return results


ob = Solution()
print(ob.possibleWords([2, 3, 4], 3))

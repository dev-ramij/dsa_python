from unittest import result


class Solution:

    def getAllMaxIdx(self, strArr):
        maxIdx = []
        max = self.getMax(strArr)
        for i in range(len(strArr)):
            if max == int(strArr[i]):
                maxIdx.append(i)
        return maxIdx

    def getMax(self, strArr):
        maxV = int(strArr[0])
        for i in range(len(strArr)):
            if maxV < int(strArr[i]):
                maxV = int(strArr[i])
        return maxV

    def swapNumbers(self, str, swap, idx, result):
        res = []
        if swap == 0 or idx == len(str) - 1:
            result.append("".join(str))
            return
        maxIdxs = self.getAllMaxIdx(str[idx:])
        if int(str[idx]) == int(str[maxIdxs[0] + idx]):
            self.swapNumbers(str, swap, idx + 1, result)
        else:
            for i in maxIdxs:
                temp = str[:]
                temp[idx], temp[i + idx] = temp[i + idx], temp[idx]
                res.append(temp)
            for i in res:
                self.swapNumbers(i, swap - 1, idx + 1, result)

    def findMaximumNum(self, s, k):
        strArr = []
        results = []
        for value in s:
            strArr.append(value)

        self.swapNumbers(strArr, k, 0, results)
        return self.getMax(results)


objects = Solution()
print(objects.findMaximumNum("4551711527", 3))

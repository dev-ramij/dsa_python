# Given two integers a and b, return the sum of the two integers without using the operators + and -.


class Solution(object):

    def getSum(self, a, b):
        sum = 0
        i = 0
        rem = 0
        first = a
        second = b
        while True:
            remA = first % 2
            remB = second % 2
            if (first > 0 or second > 0) or rem > 0:
                if (remA == 1 and remB == 0) or (remA == 0 and remB == 1):
                    sum += pow(2, i) + rem
                    rem = 0
                    first = first // 2
                    second = second // 2
                    i += 1
                    continue
                elif (remA == 1 and remB == 1):
                    sum += pow(2, i) + rem
                    rem = 1
                    first = first // 2
                    second = second // 2
                    i += 1
                    continue
                elif (remA == 0 and remB == 0):
                    rem = 0
                    first = first // 2
                    second = second // 2
                    i += 1
                    continue
                else:
                    sum += pow(2, i)
                    return sum
            else:
                return sum


obj = Solution()
print(obj.getSum(8, 10))

# The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
# Note: There may be multiple possible solutions. Return any one of them. Any correct solution will result in an output of 1, whereas wrong solutions will result in an output of 0.


class Solution:

    def stockBuySell(self, A, n):
        buy = 0
        results = []
        for i in range(1, n):
            if A[buy] >= A[i]:
                if buy != i - 1:
                    results.append([buy, i - 1])
                buy = i
            if i == n - 1:
                if buy != i and A[i] > A[buy]:
                    results.append([buy, i])

        return results


obj = Solution()
print(obj.stockBuySell([100, 180, 260, 310, 40, 535, 695], 7))

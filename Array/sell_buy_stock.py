class Solution(object):

    def maxProfit(self, prices):
        max_profit = 0
        for i, value in enumerate(prices):
            if i == 0:
                minimum = value
                continue
            if value > minimum:
                profit = value - minimum
                if profit > max_profit:
                    max_profit = profit
            else:
                minimum = value
        return max_profit


obj = Solution()
print(obj.maxProfit([7,6,4,3,1]))

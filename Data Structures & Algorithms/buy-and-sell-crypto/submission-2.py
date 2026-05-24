class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            profit = max(profit, prices[i] - min_price)
        return profit 
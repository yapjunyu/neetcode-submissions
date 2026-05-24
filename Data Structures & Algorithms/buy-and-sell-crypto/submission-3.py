class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = float("inf"), 0
        for p in prices:
            minPrice = min(minPrice, p)
            maxProfit = max(maxProfit, p - minPrice)
        return maxProfit
        
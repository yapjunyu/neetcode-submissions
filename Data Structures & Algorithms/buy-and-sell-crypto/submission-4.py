class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, low = 0, float("inf")
        for price in prices:
            if price < low:
                low = price
            res = max(res, price - low)
        return res
        
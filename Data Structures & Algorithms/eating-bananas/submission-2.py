class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # upper bound of k is max(piles), lower bound 1
        # search space is 1 - max(piles)
        # how to determine if he will be able to finish in h time? sum of ceil(x/k) <= h
        res = float('inf')
        l, r = 0, max(piles)
        while l <= r:
            mid = (l + r) // 2 # rate
            if mid == 0:
                break
            taken = 0
            for pile in piles:
                taken += math.ceil(pile/mid)
            if taken > h:
                l = mid + 1
            else:
                res = min(mid , res)
                r = mid - 1
        return res if res != float('inf') else 1

        
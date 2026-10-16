class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        while l < r:
            if height[l] > height[r]:
                res += max(maxRight, height[r]) - height[r]
                maxRight = max(height[r], maxRight)
                r -= 1
            else:
                res += max(maxLeft, height[l]) - height[l]
                maxLeft = max(height[l], maxLeft)
                l += 1
        return res          
        
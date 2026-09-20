class Solution:
    def trap(self, height: List[int]) -> int:
        # at every point the amount of water that can be trapped is the min of the max left and max right
        # minus the height at that point
        l, r = 0, len(height) - 1
        leftMax = rightMax = 0
        res = 0
        while l < r:
            if height[l] < height[r]:
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                r -= 1
        return res
        
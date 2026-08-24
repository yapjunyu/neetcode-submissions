class Solution:
    def trap(self, height: List[int]) -> int:
        # build an array that records the tallest bar on left and right side
        # each point can trap the minimum of the min of left and right minus height
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while l < r:
            if height[l] > height[r]:
                right_max = max(right_max, height[r])
                res += max(right_max - height[r], 0)
                r -= 1 
            else:
                left_max = max(left_max, height[l])
                res += max(left_max - height[l], 0)
                l += 1
        return res

        
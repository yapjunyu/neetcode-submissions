class Solution:
    def trap(self, height: List[int]) -> int:
        # keep track of a left max and right max
        # use 2 pointer approach 
        res = 0
        leftMax, rightMax = 0, 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                if height[l] > leftMax:
                    leftMax = height[l] # no water is trapped 
                else:
                    res += leftMax - height[l] # water is trapped because height is taller than leftMax
                l += 1
            else:
                if height[r] > rightMax:
                    rightMax = height[r]
                else:
                    res += rightMax - height[r]
                r -= 1
        return res

        
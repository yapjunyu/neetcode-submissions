class Solution:
    def trap(self, height: List[int]) -> int:
        # keep track of the tallest left and right height at each point 
        res = 0
        left, right = [0] * len(height), [0] * len(height)
        temp = 0 
        for i in range(len(height)):
            temp = max(height[i], temp)
            left[i] = temp
        temp = 0
        for i in range(len(height) - 1, -1, -1):
            temp = max(height[i], temp)
            right[i] = temp
        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]
        return res
        
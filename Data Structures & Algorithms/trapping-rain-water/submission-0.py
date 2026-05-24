class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        if n == 0:
            return res

        maxRight = [0] * n
        maxLeft = [0] * n

        maxRight[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i + 1])
        
        maxLeft[0] = height[0]
        for i in range(len(height)):
            maxLeft[i] = max(height[i], maxLeft[i - 1])

        for i in range(len(height)):
            res += min(maxRight[i], maxLeft[i]) - height[i]
        return res

        
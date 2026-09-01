class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        width = len(heights)
        for i in range(width):
            start = i
            while stack and stack[-1][1] > heights[i]:
                res = max((i - stack[-1][0]) * stack[-1][1], res)
                start = stack[-1][0]
                stack.pop()
            stack.append((start, heights[i]))
        while stack:
            res = max(res, (width - stack[-1][0]) * stack[-1][1])
            stack.pop()
        return res
        
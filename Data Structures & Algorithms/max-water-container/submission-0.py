class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        while l < r: 
            area = (r - l) * min(heights[l], heights[r])
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
            res = max(area, res)
        return res

        
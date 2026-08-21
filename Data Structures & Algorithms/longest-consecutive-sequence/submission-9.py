class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # only start building the sequence if num - 1 dont exist
        a = set(nums)
        res = 0
        for num in a:
            if num - 1 not in a:
                count = 1
                temp = num
                while temp + 1 in a:
                    count += 1
                    temp += 1
                res = max(count, res)
        return res
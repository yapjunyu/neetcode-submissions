class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn it into a set for O(1) lookup
        res = 0
        nums = set(nums)
        # if the number - 1 does not exist in the set, can start to build the sequence 
        for num in nums:
            if (num - 1) not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                res = max(res, length)
        return res
        
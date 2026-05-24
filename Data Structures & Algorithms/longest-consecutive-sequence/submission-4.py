class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn it into a set for O(1) lookup
        res = 0
        count = 0
        nums = set(nums)
        # if the number - 1 does not exist in the set, can start to build the sequence 
        for num in nums:
            if num - 1 in nums:
                continue
            else:
                while num + count in nums:
                    count += 1
            res = max(count, res)
            count = 0 
        return res
        
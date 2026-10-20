class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start building the sequence if there is no val - 1 in the arr
        # turn into a set for o(1) look up 
        hmap = set(nums)
        res = 0
        for val in hmap:
            if (val - 1) not in hmap:
                count = 0
                while val + count in hmap:
                    count += 1
                res = max(res, count)
        return res

        
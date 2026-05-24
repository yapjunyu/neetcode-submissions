class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert array to hash set to get O(1) lookup
        # only start building a sequence when num - 1 is not in the set
        a = set(nums)
        result = 0
        for num in a:
            if (num - 1) not in a:
                length = 1
                while num + length in a:
                    length += 1
                result = max(result, length)
        return result

        
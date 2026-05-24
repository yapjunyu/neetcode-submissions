class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert array to hash set to get O(1) lookup
        # only start building a sequence when num - 1 is not in the set
        a = set(nums)
        result = 0
        for num in a:
            seq = []
            if ((num - 1) not in a):
                count = num
                while count in a:
                    seq.append(count)
                    count += 1
                result = max(result, len(seq))
        return result

        
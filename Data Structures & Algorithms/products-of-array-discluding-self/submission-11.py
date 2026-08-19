class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix
        # res = []
        # prefix, suffix, = 1, 1
        # for i in range(len(nums)):
        #     if i != 0:
        #         prefix *= nums[i - 1]
        #     res.append(prefix)
        # for i in range(len(nums) - 1, -1, -1):
        #     if i != len(nums) - 1:
        #         suffix *= nums[i + 1]
        #     res[i] *= suffix
        # return res
        res = [1] * len(nums)
        prefix, suffix = 1, 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            res[i] *= prefix
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
        
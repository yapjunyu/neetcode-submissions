class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix suffix
        res = []
        prefix = 1 
        suffix = 1
        for num in nums:
            res.append(prefix)
            prefix *= num
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
        
        
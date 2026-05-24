class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        pos = [1] * len(nums)
        num1 = 1
        num2 = 1
        result = []
        for i in range(len(nums) + 1):
            if i != 0:
                pos[i - 1] = num1
                num1 *= nums[i - 1]
            if i != len(nums):
                pre[len(nums) - i - 1] = num2
                num2 *= nums[len(nums) - i - 1]
        for x in range(len(nums)):
            result.append(pos[x] * pre[x])
        return result
            

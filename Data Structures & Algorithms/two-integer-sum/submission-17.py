class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder not in a:
                a[nums[i]] = i
            else:
                return [a[remainder], i]
            
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in a:
                return [a.get(difference), i]
            a[nums[i]] = i
    

        
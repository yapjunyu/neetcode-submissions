class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashmap to keep track of the remainder
        hmap = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder not in hmap:
                hmap[nums[i]] = i
            else:
                return [hmap[remainder], i]
            
        
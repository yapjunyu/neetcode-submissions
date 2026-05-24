class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # if the smallest number is bigger than 0, there will nvr be a combination
            if num > 0:
                break
            
            # skip if the number is the same as previous to avoid duplicates
            if i > 0 and nums[i - 1] == num:
                continue
        
            l, r = i + 1, len(nums) - 1
            while l < r:
                target = num + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

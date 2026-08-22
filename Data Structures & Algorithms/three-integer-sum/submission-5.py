class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # break it down into 2 pointer aproach, fix one number and then find the other 2 
        # i + j + k = 0
        # j + k = -i 
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            if nums[i] > 0:
                break

            l, r = i + 1, len(nums) - 1
            target = nums[i] * -1
            while l < r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif target > total:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
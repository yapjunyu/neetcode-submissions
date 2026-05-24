class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l, r = 0, len(numbers) - 1
        # while numbers[l] + numbers[r] != target:
        #     while numbers[l] + numbers[r] > target:
        #         r -= 1
        #     while numbers[l] + numbers[r] < target:
        #         l += 1
        # return [l + 1, r + 1]
        diff = {}
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in diff:
                return [diff.get(difference) + 1, i + 1]
            diff[numbers[i]] = i
                
        
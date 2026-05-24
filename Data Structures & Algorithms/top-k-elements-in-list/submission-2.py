class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)
        res = []
        for i in counter:
            count[counter[i]].append(i)
        for i in range(len(count) - 1, -1, -1):
            for val in count[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
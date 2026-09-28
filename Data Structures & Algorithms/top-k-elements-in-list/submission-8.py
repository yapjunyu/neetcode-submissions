class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key in count.keys():
            bucket[count[key]].append(key)
        res = []
        for arr in bucket[::-1]:
            for el in arr:
                res.append(el)
                if len(res) == k:
                    return res
        return res


        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []
        l = 0
        for r in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[r], r))
            if r >= k - 1:
                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
                l += 1
        return res
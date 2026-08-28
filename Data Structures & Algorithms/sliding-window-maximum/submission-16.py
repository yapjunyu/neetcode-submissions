class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a queue
        q = deque()
        res = []
        for i in range(len(nums)):
            count = 0
            while q and q[-1] < nums[i]:
                q.pop()
                count += 1
            q.extend([nums[i]] * count)
            q.append(nums[i])
            if i >= k - 1:
                res.append(q[0])
                q.popleft()
        return res

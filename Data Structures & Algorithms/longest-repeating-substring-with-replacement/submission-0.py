class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}

        l = 0
        maxFreq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])

            while r - l + 1 - maxFreq > k:
                # when shifting the left pointer, we dont need to update the maxfreq
                # because we are only looking for a bigger max freq to get a better result
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

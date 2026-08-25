class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replace into the most common letter in the window
        res, l, maxFreq = 0, 0, 0
        a = {}
        for i in range(len(s)):
            a[s[i]] = a.get(s[i], 0) + 1
            maxFreq = max(maxFreq, a[s[i]])
            while i - l + 1 - maxFreq > k:
                a[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res 

        
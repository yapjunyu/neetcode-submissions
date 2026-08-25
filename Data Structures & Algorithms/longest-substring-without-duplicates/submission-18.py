class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # need to keep track of the last index of the character
        # shrink the window to that index 
        res, l = 0, 0
        a = {}
        for i in range(len(s)):
            if s[i] in a:
                l = max(l, a[s[i]] + 1)
            a[s[i]] = i
            res = max(res, i + 1 - l)
        return res
        
        
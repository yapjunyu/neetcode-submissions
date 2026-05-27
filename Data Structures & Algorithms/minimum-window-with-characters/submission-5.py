class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tCount, window = {}, {}
        res, resLen = [-1, -1], float("inf")
        l = 0

        for ch in t:
            tCount[ch] = tCount.get(ch, 0) + 1
        have, need = 0, len(tCount)
        
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1
            if ch in t and window[ch] == tCount[ch]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in t and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1] + 1] if resLen != float("inf") else ""
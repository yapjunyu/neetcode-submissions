class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count, window = {}, {}
        res, reslen = [-1, -1], float("infinity")

        for ch in t:
            count[ch] = count.get(ch, 0) + 1
        
        have, need = 0, len(count)
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1] + 1] if reslen != float("infinity") else ""
        
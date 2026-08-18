class Solution:

    def encode(self, strs: List[str]) -> str:
        # append the length of str followed by a special character
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while l < len(s):
            index = s.find("#", l)
            length = int(s[l:index])
            l = index + 1
            r = l + length
            res.append(s[l:r])
            l = r
        return res


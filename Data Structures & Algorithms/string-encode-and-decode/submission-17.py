class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode with the lenght of the string + a special character
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while l < len(s):
            temp = s[l:].find('#')
            r += temp
            length = int(s[l:r]) 
            l = r + 1
            r = l + length
            word = s[l:r]
            res.append(word)
            l = r 
        return res 

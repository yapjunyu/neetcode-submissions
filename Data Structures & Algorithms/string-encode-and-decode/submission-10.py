class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode str with the len of str plus a separator '&'
        res = ""
        for s in strs:
            res += str(len(s)) + '&' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        cur = 0
        while len(s):
            sep = s.find('&')
            length = int(s[:sep]) + 1
            word = s[sep + 1: sep + length]
            print(word)
            res.append(word)
            cur = sep + length
            s = s[cur::]
        return res

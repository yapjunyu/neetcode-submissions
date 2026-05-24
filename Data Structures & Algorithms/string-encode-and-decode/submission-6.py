class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s):
            if s[i] != '#':
                i += 1
            else:
                num = int(s[j:i])
                j = i + 1
                i = j + num
                print(s[j:i])
                res.append(s[j:i])
                j = i
        return res    

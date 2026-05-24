class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        a, b = 0, 0 
        res = []

        while a < len(s):
            if s[a] != "#":
                a += 1
            else:
                num = int(s[b:a])
                b = a + 1
                a = b + num
                res.append(s[b:a])
                b = a
        return res

class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode with a symbol and then the length of the string
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        # use 2 pointer to navigate the array
        a = 0
        b = 0 
        res = []
        while a != len(s):
            if s[a] != "#":
                a += 1
            else:
                count = int(s[b:a])
                b = a + 1
                a = b + count
                res.append(s[b:a])
                b = a
        return res
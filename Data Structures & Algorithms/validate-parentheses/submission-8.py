class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {"}":"{","]":"[",")":"("}
        for ch in s:
            if ch in hmap:
                if stack and stack[-1] == hmap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
        
        
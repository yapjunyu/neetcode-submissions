class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(","}":"{","]":"["}

        for ch in s:
            if stack and ch in mapping:
                if stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return False if stack else True
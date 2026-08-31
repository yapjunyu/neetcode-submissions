class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack to store the indices 
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
        
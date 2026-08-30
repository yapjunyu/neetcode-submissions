class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use a stack to store the results
        import operator
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        stack = []
        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                res = operations[i](b, a)
                stack.append(res)
        return int(stack[0])

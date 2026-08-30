class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use a stack to store the results
        import operator
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda b, a: int(b / a),
        }
        stack = []
        for i in tokens:
            if i not in operations:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                res = operations[i](b, a)
                stack.append(res)
        return stack[0]

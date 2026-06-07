class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
            ops = ['+', '-', '*', '/']
            stack = []
            for token in tokens:
                if token in ops:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    if token == "+":
                        stack.append(op1 + op2)
                    elif token == "-":
                        stack.append(op1 - op2)
                    elif token == "*": 
                        stack.append(op1 * op2)
                    else:
                        stack.append(int(op1 / op2)) 
                else:
                    stack.append(int(token))
            return stack[-1]
        
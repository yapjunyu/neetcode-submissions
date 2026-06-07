class MinStack:

    def __init__(self):
        self.stack = []
        self.pstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.pstack:
            self.pstack.append(min(self.pstack[-1], val))
        else:
            self.pstack.append(val)
    

    def pop(self) -> None:
        self.stack.pop()
        self.pstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.pstack[-1]
        

class MinStack:

    def __init__(self):
        self.stack = []
        self.minTracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minTracker:
            val = min(val, self.minTracker[-1])
        self.minTracker.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minTracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minTracker[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2
class MinStack:
    def __init__(self):
        self.minValue = pow(2, 31)
        self.element = []
    def push(self, val: int) -> None:
        self.element.append(val)
        if self.minValue > val:
            self.minValue = val
    def pop(self) -> None:
        self.element.pop()
        self.minValue = min(self.element) if len(self.element)>0 else pow(2, 31)
    def top(self) -> int:
        return self.element[-1]
    def getMin(self) -> int:
        return self.minValue
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

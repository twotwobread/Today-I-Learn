class MyQueue:

    def __init__(self):
        self.l = []
        self.length = 0
    def push(self, x: int) -> None:
        self.l.append(x)
        self.length += 1
    def pop(self) -> int:
        if not self.empty():
            temp = self.l
            self.l = self.l[1:]
            self.length -= 1
            return temp[0]
        else:
            print("Queue is Empty!!")
            return -1;

    def peek(self) -> int:
        return self.l[0]

    def empty(self) -> bool:
        if self.length == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

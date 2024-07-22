class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        s2 = []
        for _ in range(len(self.s)):
            s2.append(self.s.pop())
        s2.append(x)
        for _ in range(len(s2)):
            self.s.append(s2.pop())

    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return len(self.s) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
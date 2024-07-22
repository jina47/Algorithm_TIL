from collections import deque as dq

class MyStack:

    def __init__(self):
        self.q1 = dq([])
        self.size = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.size += 1

    def pop(self) -> int:
        q2 = dq([])
        for _ in range(self.size-1):
            q2.append(self.q1.popleft())
        value = self.q1.popleft()
        self.q1 = q2
        self.size -= 1
        return value


    def top(self) -> int:
        q2 = dq([])
        for _ in range(self.size-1):
            q2.append(self.q1.popleft())
        value = self.q1.popleft()
        q2.append(value)
        self.q1 = q2
        return value

    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
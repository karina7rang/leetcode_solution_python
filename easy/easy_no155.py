class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mylist = []

    def push(self, x: int) -> None:
        self.mylist.append(x)

    def pop(self) -> None:
        self.mylist.pop()

    def top(self) -> int:
        return self.mylist[-1]

    def getMin(self) -> int:
        return min(self.mylist)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []

    def push(self, x: int) -> None:
        self.res.append(x)

    def pop(self) -> None:
        self.res.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        return min(self.res)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
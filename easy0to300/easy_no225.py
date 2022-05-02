class MyStack:

    def __init__(self):
        self.ls = []
        
    def push(self, x: int) -> None:
        self.ls.append(x)
        
    def pop(self) -> int:
        return self.ls.pop()

    def top(self) -> int:
        return self.ls[-1]

    def empty(self) -> bool:
        if self.ls==[]:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class MyStack:

    def __init__(self):
        self.ls = list()
        
    def push(self, x: int) -> None:
        self.ls.append(x)
        
    def pop(self) -> int:
        return self.ls.pop()

    def top(self) -> int:
        return self.ls[-1]

    def empty(self) -> bool:
        if len(self.ls)==0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyStack:

    def __init__(self):
        self.ls = deque()
        
    def push(self, x: int) -> None:
        self.ls.append(x)
        
    def pop(self) -> int:
        return self.ls.pop()

    def top(self) -> int:
        return self.ls[-1]

    def empty(self) -> bool:
        if len(self.ls)==0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
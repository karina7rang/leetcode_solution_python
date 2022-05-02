# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        self.cycle = False
        self.res = {}
        
        def myfunc(node):
            if node:
                if node in self.res:
                    self.cycle = True
                else:
                    self.res[node] = 0
                    myfunc(node.next)
        
        myfunc(head)
        # print(self.res)
        return self.cycle


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        check = []
        while node:
            if node in check:
                return True
            check.append(node)
            node = node.next
        return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        self.res = False
        def check(node, ls):
            if node:
                if node in ls:
                    self.res = True
                else:
                    ls.append(node)
                    check(node.next, ls)
        check(head,[])
        return self.res

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        def check(node, ls):
            if node:
                if node in ls:
                    return True
                else:
                    ls.append(node)
                    return check(node.next, ls)
            else:
                return False
        return check(head,[])


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head and head.next and head.next.next:
            slow = head
            fast = head.next.next
            while slow and fast:
                if slow==fast:
                    return True
                else:
                    try:
                        slow = slow.next
                        fast = fast.next.next
                    else:
                        return False
        else:
            return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head and head.next and head.next.next:
            slow = head
            fast = head.next.next
            while slow and fast:
                if slow==fast:
                    return True
                else:
                    if not fast.next:
                        return False
                    else:
                        slow = slow.next
                        fast = fast.next.next
        else:
            return False
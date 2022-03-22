# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        
        self.tmp = {}
        def myfunc(node):
            if node:
                self.tmp[node]=0
                # self.tmp.append(node)
                myfunc(node.next)
                
        myfunc(headA)
        
        self.res = None
        node = headB
        while node:
            if node in self.tmp:
                self.res = node
                break
            else:
                node=node.next
        return self.res
        

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        b = headB
        while headA:
            while b:
                if headA==b:
                    return headA
                else:
                    b=b.next
            headA=headA.next
            b = headB
        return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lsa = []
        while headA:
            lsa.append(headA)
            headA = headA.next
        while headB:
            if headB in lsa:
                return headB
            else:
                headB=headB.next
        return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lsa = {}
        while headA:
            lsa[headA]=0
            headA = headA.next
        while headB:
            if headB in lsa:
                return headB
            else:
                headB=headB.next
        return None